# 🦁 男友求生翻譯機 (Girlfriend Translator)

本專案採用 **CRISP-DM (Cross-Industry Standard Process for Data Mining)** 跨產業資料探勘標準流程進行開發與文件撰寫。

---

## 1. 商業理解 (Business Understanding)

### 專案背景
在現代情侶關係中，「溝通」往往是最大的挑戰。女朋友說的話經常隱含深層語意，而直男男友往往只聽懂字面意思，導致無數的誤會與「送命題」。

### 商業目標
-   **降低溝通成本**：透過 AI 翻譯，減少情侶間因語意理解錯誤而產生的爭執。
-   **提高存活率**：為男友提供「求生型」的最佳回覆建議，確保生命安全。
-   **情感潤滑劑**：以幽默風趣的方式化解緊張氣氛。

---

## 2. 資料理解 (Data Understanding)

### 資料來源
-   **使用者輸入**：由使用者（男友）輸入女朋友說的一句話或一段文字。
-   **語境假設**：模型預設語境為「情緒複雜、話中有話」的情侶對話場景。

### 資料特性
-   非結構化文本數據。
-   高度依賴語境 (Context-dependent)。
-   含蓄、隱喻性強 (Implicit)。

---

## 3. 資料準備 (Data Preparation)

### 提示工程 (Prompt Engineering)
我們不對使用者輸入進行傳統的資料清洗，而是透過精心設計的 **System Prompt** 來引導模型進行資料轉換：
-   **角色設定**：「求生型男友翻譯 AI」。
-   **轉換邏輯**：將輸入文本映射至四個維度：
    1.  **官方說法** (Official Statement)
    2.  **內心 OS** (Inner Monologue)
    3.  **真正意思** (Real Meaning)
    4.  **求生回覆** (Survival Reply)

---

## 4. 建模 (Modeling)

### 技術架構
-   **核心模型**：利用 `aisuite` 整合多種 LLM (如 Llama 3, GPT-4o, Mistral)。
-   **應用框架**：使用 `Streamlit` 快速建構互動式 Web App。

### 選擇理由
-   **aisuite**：提供統一介面，可靈活切換不同供應商的模型，無需大幅修改程式碼。
-   **Generative AI**：傳統 NLP 難以處理極度依賴語境的「弦外之音」，生成式 AI 在此類語意推理上表現卓越。

---

## 5.評估 (Evaluation)

### 驗證方式
-   **主觀測試**：輸入經典送命題（如：「沒事，你去忙吧」），檢查 AI 解析是否精準且具幽默感。
-   **功能測試**：確認 API Key 切換、錯誤處理（Error Handling）是否正常運作。

### 當前成果
系統能成功識別反諷、情緒勒索等高階語意，並給出具建設性（且保命）的回覆建議。

---

## 6. 部署 (Deployment)

### 執行環境
本專案為輕量級 Web 應用，可直接於本地端或雲端容器中執行。

### 啟動方式
```bash
# 安裝依賴
pip install -r requirements.txt

# 設定環境變數 (於 .env)
# GROQ_API_KEY=your_key...

# 啟動應用
python -m streamlit run app.py
```

---

## 📂 檔案結構說明

```plaintext
GirlfriendTranslator/
├── .env                # [配置] 存放 API Keys (需自行建立)
├── .gitignore          # [配置] Git 忽略清單
├── app.py              # [核心] Streamlit 主程式
├── prompt.md           # [紀錄] 開發過程對話紀錄
├── report.md           # [文件] 專案摘要 (Abstract)
├── requirements.txt    # [依賴] Python 套件清單
└── venv/               # [環境] Python 虛擬環境目錄
```
