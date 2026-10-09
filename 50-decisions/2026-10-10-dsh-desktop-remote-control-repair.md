# 决策 · DSH Desktop 远程控制采用当前 Remote 架构

Human PI 明确要求修复本机 DSH Desktop，并安装手机控制电脑的插件。

本机 Desktop `0.2.0-rc.2` 不再使用旧 `apiProxy` 服务组合；因此不采用强制挂载 `@deepseek-ai/dsh-host-apiproxy` 的混合架构。将 `@linxin666/dsh-remote-web-ui` 固定为明确支持 DSH `>=0.2.0-rc.2` 的 `0.4.5`，使用其 `webServer + typertGateway + connection` 路径。不因本次修复升级 DSH Desktop 核心。

默认运行姿态为：

- 同一可信 LAN 绑定 `0.0.0.0:19387`；
- 手机只经可撤销的配对 `/remote` 通道访问；
- 不为 LAN 主机开放直连 `/api` 信任；
- 公网快速隧道组件可用但默认关闭，不在未明确需要时把科研控制面经第三方中继暴露到公网；
- Windows 防火墙只允许 Private/Domain profile 的 TCP 19387，不创建 Public 全局放行。

该能力属于本机操作支持，不是科研证据、模型路由或记忆的信任根。更新时必须同时核对 Desktop cohort 合同和配对栅栏，不跟随 `latest` 无条件滚动。实施、验证和回滚记录见 `40-work/lab-research-os/artifacts/DSH-DESKTOP-REMOTE-CONTROL-REPAIR-2026-10-10.md`。
