import matplotlib.pyplot as plt
from PIL import Image

from vietocr.tool.predictor import Predictor
from vietocr.tool.config import Cfg
from fastapi import FastAPI, HTTPException, Query,File
import httpx
import io 

app = FastAPI()
config = Cfg.load_config_from_name('vgg_transformer')
config['cnn']['pretrained']=False
config['device'] = 'cpu'
detector = Predictor(config)

@app.get("/detect_text")

async def detect_text(image_url: str = Query(..., description="URL of the image to analyze")):
   
   return {"hoten":1}
