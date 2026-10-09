# DSH Desktop 手机远程控制修复记录

日期：2026-10-10

本机 DSH Desktop：`0.2.0-rc.2`

对象 profile：`C:/Users/ASUS/.dsh/profiles/desktop`

## 结论

DSH Desktop 启动崩溃已修复，手机远程控制插件的宿主、绑定、配对状态与安全栅栏已在本机活跃。手机实机扫码闭环仍需 Human PI 在手机上执行；Windows 防火墙规则因需管理员权限尚未写入。

## 根因

1. 最初崩溃由 `@nn12138/dsh-voice` 在 Desktop 组合中缺少 `webServer` 注入引起。语音行和直接依赖已从活跃 profile 移除，安装前备份保留。
2. 第二次崩溃由 `@linxin666/dsh-remote-web-ui 0.2.9` 强制注入旧 `apiProxy` 服务引起。当前 Desktop `0.2.0-rc.2` 使用新远程接口组合，不应强行混入旧网关。
3. 上游当前版本 `@linxin666/dsh-remote-web-ui 0.4.5` 明确声明 DSH `>=0.2.0-rc.2`，并改用 `webServer + typertGateway + connection`，与本机 Desktop cohort 一致。

## 已实施

- 将远控插件从 `0.2.9` 原位升级并固定到 `0.4.5`。
- 从 profile 依赖中移除不再需要的 `@deepseek-ai/dsh-host-apiproxy 0.1.1-rc.2`。
- 将局域网绑定改为插件可识别的 managed block：`0.0.0.0:19387`，同时保留 gzip 压缩参数。
- 设置 `lanBind: true`、`autoTunnel: false`；默认优先同一可信局域网的配对通道，不把 LAN 主机加入直连 `/api` 信任列表。
- 已允许并安装该插件声明的 `cloudflared 0.7.3` 平台二进制，但公网快速隧道仍默认关闭。
- 启动动画插件保留，未修改科研模型路由、任务或凭据。

## 验证证据

- Desktop 正常启动并显示现有会话窗口；2026-10-08 修复后至 2026-10-10 未产生新的 host crash log。
- `0.0.0.0:19387` 正在监听，所属进程为 DSH Desktop。
- `GET /api/pair/status` 在回环与 LAN 地址均返回 200，报告 `lanAvailable: true`。
- 插件自检报告 `10.190.28.65:19387 exposed: false`。
- 未配对的 `GET /remote/api/session.list` 返回 403 `unpaired`。
- LAN 上直接 `GET /api/session.list` 返回 401 `unauthorized`；未开放宿主 API。
- 配对库中保留 4 条既有设备记录，验证时在线数为 0；未自动撤销用户设备。

## 未完成 / 最小下一步

`/api/pair/lan-bind` 报告防火墙 `ok: false, managed: true`。插件自动写入、非提权命令和一次 UAC 提权启动共达到同一失败类的三次上限；最后一次在系统层被取消，未继续重试。

如手机同一 Wi-Fi 下无法连接，以管理员身份运行：

```powershell
netsh advfirewall firewall add rule name="remote-web-ui (auto)" dir=in action=allow protocol=TCP localport=19387 profile=private,domain
```

然后在 DSH Desktop 侧边栏设置按钮旁点手机图标，刷新二维码并用手机扫码。只有手机扫码后的实际会话控制成功，才可将端到端状态升级为 VERIFIED。

## 回滚

修复前文件保留在：

- `C:/Users/ASUS/.dsh/profiles/desktop/package.json.bak-20261008-pre-remote-045`
- `C:/Users/ASUS/.dsh/profiles/desktop/cordis.patch.yml.bak-20261008-pre-remote-045`

回滚时先退出 DSH Desktop，恢复这两个文件后在 profile 中重新安装依赖。旧 `0.2.9` 本身与当前 Desktop 运行架构不兼容，因此回滚仅用于诊断，不是建议的长期状态。
