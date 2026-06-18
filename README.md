# Stellar Community Bot

> 專為 Discord 車隊社群打造的身分組管理與社群營運機器人。

Stellar Community Bot 是一套專為《世界計畫》Discord 車隊社群設計的管理機器人。

主要負責身分組領取、社群規章發送、新成員歡迎、成員統計與日常管理功能，協助管理團隊維持良好的社群秩序與使用體驗。

本專案目前為 **Stellar 車隊專用版本**，採單伺服器設計，不提供多伺服器支援。

---

## ✨ 功能特色

### 📜 社群規章管理

* 發送車隊群規嵌入訊息
* 集中管理社群規範
* 支援管理員斜線指令操作

### 🎭 身分組自助領取

支援透過反應領取或移除身分組。

目前支援：

* 車隊成員身分組
* 推團身分組
* 推角身分組
* 特殊通知身分組
* 分隔線身分組

### 👋 新成員歡迎系統

* 自動發送歡迎訊息
* 顯示目前伺服器成員數
* 引導新成員完成初始設定

### 📊 車隊成員統計

* 自動統計車隊成員數量
* 即時更新統計頻道名稱

### 🛡️ 社群管理工具

* 警告系統
* 清除訊息指令
* 管理員權限驗證

---

## 🛠️ 技術棧

* Python 3.13
* discord.py 2.x
* python-dotenv

---

## 📁 專案結構

```text
stellar-community-bot/
├─ .env
├─ main.py
├─ requirements.txt
├─ README.md
└─ assets/
```

---

## 🚀 快速開始

### 1. 複製專案

```bash
git clone <repository-url>
cd stellar-community-bot
```

### 2. 建立虛擬環境

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. 安裝套件

```bash
pip install -r requirements.txt
```

---

## ⚙️ 環境變數設定

建立 `.env` 檔案：

```env
DISCORD_TOKEN=YOUR_BOT_TOKEN
```

---

## 🔑 Discord Developer Portal 設定

請於 Discord Developer Portal 啟用以下 Intents：

* Server Members Intent
* Message Content Intent

並確認機器人具有以下權限：

* Manage Roles
* Manage Messages
* Read Messages/View Channels
* Send Messages
* Embed Links
* Add Reactions
* Read Message History

---

## ▶️ 啟動機器人

```bash
python main.py
```

啟動成功後將顯示：

```text
========================================
🌟 【Stellar】車隊中控機器人已成功啟動！
========================================
```

---

## 🧩 主要指令

### 管理員指令

| 指令          | 說明         |
| ----------- | ---------- |
| `/發送車隊群規`   | 發送車隊規章     |
| `/發送車隊成員領取` | 建立車隊成員領取面板 |
| `/發送推團選擇`   | 建立推團身分組面板  |
| `/發送推角卡片`   | 建立推角身分組面板  |
| `/發送特殊身份領取` | 建立特殊身分組面板  |
| `/發送分隔線領取`  | 建立分隔線身分組面板 |
| `/clear`    | 清除指定數量訊息   |

### 一般功能

* 反應領取身分組
* 取消反應移除身分組
* 新成員歡迎通知
* 車隊成員數統計更新

---

## ⚠️ 注意事項

* 本專案採單伺服器設計。
* 所有 Discord ID 均直接寫入程式碼。
* 新增身分組或調整頻道時，需要同步更新設定常數。
* 機器人的身分組必須高於所有可管理身分組。

---

## 🗺️ 未來規劃

* [ ] 將設定抽離至獨立設定檔
* [ ] 支援 JSON 設定管理
* [ ] 模組化重構（Cogs）
* [ ] 完善錯誤處理機制
* [ ] 支援操作日誌記錄
* [ ] 支援多語系訊息模板

---

## 📄 授權

本專案僅供 Stellar 車隊內部使用。

未經授權，不得用於商業用途或重新散布。

---

## 👨‍💻 開發者

Stellar 管理團隊

Designed and maintained for the Stellar Discord community.
