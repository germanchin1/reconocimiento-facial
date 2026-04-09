from fastapi import FastAPI, File, UploadFile
from deepface import DeepFace
import shutil
import os

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/verify")
async def verify_img(img1: UploadFile = File(...), img2: UploadFile = File(...)):
    path1 = f"temp_{img1.filename}"
    path2 = f"temp_{img2.filename}"
    try:
        # --- PASO A: Guardar imágenes temporales ---
        with open(path1, "wb") as buffer:
            shutil.copyfileobj(img1.file, buffer)
        with open(path2, "wb") as buffer:
            shutil.copyfileobj(img2.file, buffer)
        
        # --- PASO B: Llamada a la IA ---
        result = DeepFace.verify(
            img1_path=path1,
            img2_path=path2,
            model_name='Facenet',
            detector_backend='opencv',
            enforce_detection=True
        )
        return {
            "verified": bool(result["verified"]),
            "distance": float(result["distance"]),
            "model": result["model"]
        }
    except Exception as e:
        return {"error": str(e)}
    finally:
        # Limpieza de archivos
        if os.path.exists(path1):
            os.remove(path1)
        if os.path.exists(path2):
            os.remove(path2)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
