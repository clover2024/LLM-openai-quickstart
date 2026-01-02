import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import ArgumentParser, ConfigLoader, LOG
from model import GLMModel, OpenAIModel
from translator import PDFTranslator

if __name__ == "__main__":

    # 不用命令行传参，全部写到配置文件
    config_loader = ConfigLoader(os.path.join(os.path.dirname(__file__), "../config.yaml"))
    config = config_loader.load_config()

    if config['OpenAIModel']['if_use']:
        api_key = config['OpenAIModel']['api_key']
        model_name = config['OpenAIModel']['model']
        model = OpenAIModel(model=model_name, key=api_key)
    else:
        api_key = config['GLMModel']['api_key']
        model_name = config['GLMModel']['model']
        model = GLMModel(model=model_name, key=api_key)

    pdf_file_path = config['common']['book']
    file_format = config['common']['file_format']
    target_language = config['common']['target_language']

    # 实例化 PDFTranslator 类，并调用 translate_pdf() 方法
    translator = PDFTranslator(model)
    translator.translate_pdf(pdf_file_path, file_format, target_language)
