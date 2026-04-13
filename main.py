from fastapi import FastAPI

#Inicializar o FastAPI
app = FastAPI(tittle="Gesão escolar")

#Rota
@app.get("/")
def tela_inicial():
    return {"mensagem": "Bem-vindo ao sistema de gestão escolar"}

#Rodar api
# no terminal: python -m uvicorn main:app --reload

#Rota de dados
alunos = {
    1: {"nome": "Gabriel", "idade": 34},
    2: {"nome": "Cassio", "idade": 67},
    3: {"nome": "Balder", "idade": 69},
}

@app.get("/alunos")
def listar_alunos():
    return {f"lista de alunos": alunos}