from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
import os

app = FastAPI()

# 파일이 저장된 디렉토리 경로 (백엔드 서버 내부 컨픽과 매핑)
file_directory = 'C:/AWP/file'


@app.get('/{filename}', response_class=FileResponse)
def serve_file(filename: str):
    file_path = os.path.join(file_directory, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        raise HTTPException(status_code=404, detail="File not found")


@app.get('/', response_class=HTMLResponse)
def index():
    return "hello!"


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
