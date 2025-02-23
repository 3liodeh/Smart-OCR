from OCR import ImageOCR, VideoOCR
from LLM import (GeminiLLM, chat_with_video, 
                 initialize_llm)

def extract_image(file_path):
    ocr_result = ImageOCR(file_path)
    
    return ocr_result

def extract_video(file_path):
    
    ocr_result = VideoOCR(file_path)
    
    return ocr_result


def AI(Query ,model, memory):
    
    response = chat_with_video(Query, model, memory)
    
    return response




        
