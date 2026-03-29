from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from rembg import remove

app = FastAPI()

# Crucial: This allows your Vercel frontend to communicate with this Render backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # You can change this to your Vercel URL later for security
    allow_credentials=false,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return {"status": "PALMTOOLS AI Backend is running!"}

@app.post("/remove-bg")
async def remove_background(image: UploadFile = File(...)):
    # Read the uploaded image bytes
    input_image = await image.read()
    
    # Run the rembg AI model
    output_image = remove(input_image)
    
    # Send the transparent PNG back to the browser
    return Response(content=output_image, media_type="image/png")
