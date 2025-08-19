# 中弘VRF网关 (绿米版) Home Assistant集成

**[English → README_EN.md](./README_EN.md)**

集成使用了HTTP+TCP混合的方式解决了原有HTTP方式响应延迟的问题，使用体验更友好。

> [!WARNING]
> 
> 该集成仅适用于中弘VRF绿米版本的网关，经过重置，现在支持多个外机（仅测试到2个）

# 安装方式

## 使用 HACS 安装

[![打开 Home Assistant 并打开 HACS商店内的存储库。](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=Johnnybyzhang&repository=Zhong_Hong_VRF&category=integration)

## 手动安装

将 `custom_components` 下的 `zhong_hong_vrf` 文件夹到 Home Assistant 中的`custom_components` 目录，并手动重启 Home Assistant。

# 设置

[![打开 Home Assistant 并设置新的集成。](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=zhong_hong_vrf)

> [!CAUTION]
> 
> 如果您无法使用上面的按钮，请按照以下步骤操作：
> 
> 1. 导航到 Home Assistant 集成页面（设置 --> 设备和服务）
> 2. 单击右下角的 `+ 添加集成` 按钮
> 3. 搜索 `Zhong Hong VRF`

> [!NOTE]
> 
> 1. 网关IP请填写VRF的IP地址
> 2. TCP端口默认为`9999`
> 3. 用户名默认为`admin`
> 4. 密码默认为空

# 卸载说明

要从 Home Assistant 中完全移除中弘VRF集成：

## 通过 Home Assistant 界面卸载（推荐）

1. 导航到 **设置** → **设备和服务**
2. 在集成列表中找到 **中弘VRF** 集成
3. 点击集成条目进入详情页面
4. 点击右上角的 **三点菜单** (⋮)
5. 选择 **移除** 并确认移除操作
6. 集成及所有关联的设备/实体将自动被移除

## 清理残留的设备/实体（如有需要）

如果移除后仍有孤立的设备或实体：

1. 前往 **设置** → **设备和服务** → **设备** 选项卡
2. 查找任何名称包含"中弘VRF"或"空调"的设备
3. 点击每个设备并选择 **删除设备**
4. 前往 **设置** → **设备和服务** → **实体** 选项卡
5. 筛选包含"zhong_hong"或您的空调设备名称的实体
6. 选择并移除任何残留实体

## 手动文件移除（如有需要）

如果是手动安装且想要完全移除文件：

1. 停止 Home Assistant
2. 导航到您的 `custom_components` 目录
3. 删除 `zhong_hong_vrf` 文件夹
4. 重启 Home Assistant

## 重新添加集成

要在移除后重新添加集成：
- 只需按照上面的 **设置** 说明操作即可
- 所有设备将被自动重新发现
- 之前的实体名称和自定义配置需要重新设置

# 支持的空调品牌

本集成支持广泛的空调品牌，包括：
- **主要品牌**：日立、大金、东芝、三菱重工、三菱电机、格力、美的、海尔、三星、LG
- **中国品牌**：海信、奥克斯、志高、TICA、TCL
- **专用系统**：协议转换器、温控器、模块化系统
- **地区变体**：约克青岛、CH-York、酷风等

完整的支持品牌列表请查看 [`custom_components/zhong_hong_vrf/const.py`](https://github.com/Johnnybyzhang/Zhong_Hong_VRF/blob/main/custom_components/zhong_hong_vrf/const.py) 中的 `AC_BRANDS` 映射。

# 开发

本项目遵循 Home Assistant 集成最佳实践，包含完整的测试和质量保证。

## 开发命令

- `make fmt` - 使用 black 和 ruff 格式化代码
- `make lint` - 运行代码检查
- `make test` - 运行测试套件
- `make audit` - 运行安全审计
- `make install-dev` - 安装开发依赖

## 贡献

请遵循约定式提交格式：
- `feat(范围): 描述` - 新功能
- `fix(范围): 描述` - 缺陷修复
- `chore(范围): 描述` - 维护任务

所有PR必须≤300行代码且包含测试。

# Credits

[xswxm/home-assistant-zhong-hong](https://github.com/xswxm/home-assistant-zhong-hong)

---

**[English → README_EN.md](./README_EN.md)**
