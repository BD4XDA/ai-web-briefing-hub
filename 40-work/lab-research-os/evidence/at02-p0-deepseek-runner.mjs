import {createRequire} from 'node:module';
import {pathToFileURL} from 'node:url';
import {readFileSync,writeFileSync} from 'node:fs';
import {randomUUID} from 'node:crypto';
const require=createRequire('C:/Users/ASUS/.dsh/profiles/web/package.json');
const dep=async n=>import(pathToFileURL(require.resolve(n)).href);
const {installModelSelection}=await dep('@deepseek-ai/dsh-agent');
const {createUserMessage}=await dep('@deepseek-ai/dsh-llm');
export const name='lab-text-runner';
export const inject=['agents','sessions'];
export function apply(ctx){run(ctx).catch(e=>{console.error(String(e));ctx.get('appExit')(1);});}
async function run(ctx){
  await ctx.get('loader').await();
  const model=process.env.LAB_TEXT_MODEL??'deepseek-flash';
  if(!['deepseek-flash'].includes(model))throw Error('Model not in bounded text-run allowlist');
  const selection={provider:'deepseek-official',model,reasoningEffort:'off'};
  const {agent}=await ctx.agents.create({sessionId:'lab-text-'+randomUUID(),meta:{cwd:process.cwd()},agentOptions:{provider:selection.provider,model,maxTokens:1800},setup:c=>{installModelSelection(c,{current:selection,assembled:undefined});c.tools.restrict({allow:[]});}});
  await agent.whenIdle();const first=agent.session.seq;
  agent.followup(createUserMessage({content:[{type:'text',text:readFileSync(process.env.LAB_TEXT_INPUT,'utf8')}],source:{kind:'user'}}));
  await agent.whenIdle();await ctx.sessions.flush(agent.session);
  const events=agent.session.events.filter(e=>e.seq>=first);
  const messages=events.filter(e=>e.type==='assistant/message').map(e=>e.data.message.content.filter(b=>b.type==='text').map(b=>b.text).join(''));
  const end=events.findLast(e=>e.type==='turn/end');
  const result={model,provider:'deepseek-official',harness:'dsh',sessionId:agent.session.id,text:messages.at(-1),reason:end?.data?.reason,tool_calls:events.filter(e=>e.type==='tool/call').length};
  writeFileSync(process.env.LAB_TEXT_OUTPUT,JSON.stringify(result,null,2));console.log(JSON.stringify(result));ctx.get('appExit')(end?.data?.reason?.kind==='completed'?0:1);
}
