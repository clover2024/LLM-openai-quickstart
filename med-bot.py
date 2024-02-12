# 这些只是一些建议，每个人的健康状况和需求可能不同。如果有关健康的问题或症状持续存在，建议咨询医生或专业的医疗人员。
import gradio as gr

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

def initialize_MED_BOT(vector_store_dir: str="med_faq"):
    db = FAISS.load_local(vector_store_dir, OpenAIEmbeddings())
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    
    global MED_BOT    
    MED_BOT = RetrievalQA.from_chain_type(llm,
                                           retriever=db.as_retriever(search_type="similarity_score_threshold",
                                                                     search_kwargs={"score_threshold": 0.75}))
    # 返回向量数据库的检索结果
    MED_BOT.return_source_documents = True

    return MED_BOT

def med_chat(message, history):
    print(f"[message]{message}")
    print(f"[history]{history}")
    # TODO: 从命令行参数中获取
    enable_chat = True

    ans = MED_BOT({"query": message})
    # 如果检索出结果，或者开了大模型聊天模式
    # 返回 RetrievalQA combine_documents_chain 整合的结果
    if ans["source_documents"] or enable_chat:
        print(f"[result]{ans['result']}")
        print(f"[source_documents]{ans['source_documents']}")
        return ans["result"]
    # 否则输出较为保守的回答
    else:
        return "这个问题"
    

def launch_gradio():
    demo = gr.ChatInterface(
        fn=med_chat,
        title="常见医疗问题问答机器人",
        # retry_btn=None,
        # undo_btn=None,
        chatbot=gr.Chatbot(height=600),
    )

    demo.launch(share=True, server_name="127.0.0.1")

if __name__ == "__main__":
    # 初始化医疗问题问答机器人
    initialize_MED_BOT()
    # 启动 Gradio 服务
    launch_gradio()
