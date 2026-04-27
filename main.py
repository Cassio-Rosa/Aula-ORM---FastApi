from fastapi import FastAPI, Depends, Request, Form, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db
from models import Curso, Aluno

#Inicializar o FastAPI
app = FastAPI(tittle="Gesão escolar")


templates = Jinja2Templates(directory="templates")

#Rodar api
# no terminal: python -m uvicorn main:app --reload

#ROTA
# Métodos http: GET, POST, PUT, DELETE
@app.get("/")
def exibir_cadastro(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {"request": request}
    )


@app.get("/cursos/cadastro")
def exibir_cadastro(request: Request):
    return templates.TemplateResponse(
        request,
        "cadastrar_curso.html",
        {"request": request}
    )

#Rota para cadastrar um curso
@app.post("/cursos")
def criar_curso(
    nome:str = Form(...),
    carga_horaria: int = Form(...),
    descricao: str = Form(...),
    db: Session = Depends(get_db)

):
    #CADASTRAR O CURSO NO BANCO
    novo_curso = Curso(nome=nome, carga_horaria=carga_horaria, descricao=descricao)
    db.add(novo_curso)
    db.commit()

    return RedirectResponse(url="/listar", status_code=303)


@app.get("/listar")
def listar_cursos(
    request: Request,
    db: Session = Depends(get_db)
    ):

    cursos = db.query(Curso).all()
    return templates.TemplateResponse(
        request,
        "listar_cursos.html",
        {"request": request, "cursos": cursos}
    )

#Rota para deletar
@app.post("/cursos/{id}/deletar")
def deletar_curso(
    id: int, 
    db: Session = Depends(get_db)
):
    curso = db.query(Curso).get(id)

    if curso:
        db.delete(curso)
        db.commit()

    return RedirectResponse(url="/listar", status_code=303)