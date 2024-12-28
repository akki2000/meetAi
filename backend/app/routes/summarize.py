from fastapi import APIRouter, File, UploadFile
from app.utils.transcription import transcribe_audio
from app.utils.summarization import summarize_text

router = APIRouter()

@router.post("/api/summarize/")
async def summarize_meeting(file: UploadFile = File(...)):
    # Save uploaded file
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())
    
    # Transcription
    transcript = transcribe_audio(file_path)

    # Summarization
    summary = summarize_text(transcript)

    return {"transcript": transcript, "summary": summary}
