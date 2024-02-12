# LangChain 实战：医疗问题聊天机器人

## 介绍

在本文中，我们将使用 LangChain 库来构建一个医疗问题聊天机器人。 LangChain 是一个用于构建基于语言的 AI 应用的库，它提供了一系列工具和模块，使得开发者能够轻松地构建各种类型的聊天机器人。

我们将使用 LangChain 的以下功能：

- Document Transformers 文本处理模块，用于预处理和清理文本数据。
- RetrievalQA 聊天机器人模块，用于构建聊天机器人。

## 数据集

使用 ChatGLM-4 构造医疗问题问答数据的 Prompt 示例：

```text
你是中国协和医院顶级的全科医生，现在向大众普及培训医疗知识，请给出100个常见的患者提出的医疗问题及其建议解决方案。
每条以如下格式给出：
[患者问题]
[医生回答]

```

因为后台单次token的限制，只列举了20条，其余要求其继续输出或构造如下 Prompt：

```text
现在你是精神科的主任医师，列举中小学生、大学生、程序员会遇到的常见精神疾病问题与建议解决方案，15条
```

界面展示：

![ChatGLM-4](https://cdn.jsdelivr.net/gh/clover2024/img@master/imgs/chatglm.png)

## 如何运行

Git 提交已经包含了生成的 Chroma 数据库 `med_faq`，直接运行 `med-bot.py` 即可。

## 效果

Gradio 运行界面

![Gradio 运行界面](https://cdn.jsdelivr.net/gh/clover2024/img@master/imgs/med-bot-gradio.png)

后台日志展示

![后台日志展示](https://cdn.jsdelivr.net/gh/clover2024/img@master/imgs/med-bot-log.png)

基于 DjangoPeng 的 sales-chatbot 房产销售机器人开发

医疗问答机器人 med-bot 二次开发：CloverWang