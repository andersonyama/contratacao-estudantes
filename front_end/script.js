const host_api = window.HOST_API || "http://127.0.0.1:5000/";

async function postEstudante(nome, rank_universidade, cgpa, dsa_score, coding_skills, internships) {
    let url = host_api + "estudante"
    const response = await fetch(url, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({nome: nome,
                                rank_universidade: rank_universidade, 
                                cgpa: cgpa, 
                                dsa_score: dsa_score,
                                coding_skills: coding_skills,
                                internships: internships
                            })
        }
    );

    if (!response.ok) return null;
    const data = await response.json();
    return data;
}

async function getListaEstudantes() {
    let url = host_api + "estudante"
    const response = await fetch(url, {method: 'GET'});

    if (!response.ok) throw new Error("Erro ao listar resultados");

    const data = await response.json();
    return data;
}

async function estimarContratacao() {
    let nome = document.getElementById("nome").value;
    let rank_universidade = document.getElementById("rank_universidade").value;
    let cgpa = document.getElementById("cgpa").value;
    let dsa_score = document.getElementById("dsa_score").value;
    let coding_skills = document.getElementById("coding_skills").value;
    let internships = document.getElementById("internships").value;
    
    
    if (nome && rank_universidade && cgpa && dsa_score && coding_skills && internships){
        if (rank_universidade < 1 || rank_universidade > 3) {
            alert("Tier Universidade está fora do intervalo esperado (1-3)");
        } else if (cgpa < 0 || cgpa > 10) {
            alert("GPA Acumulado está fora do intervalo esperado (0-10)");
        } else if (dsa_score < 0 || dsa_score > 10) {
            alert("Nota Programação está fora do intervalo esperado (0-10)");
        } else if (coding_skills < 0 || coding_skills > 10) {
            alert("Nota DSA está fora do intervalo esperado (0-10)");
        } else if (internships < 0 || internships > 3) {
            alert("Qtd Estágios está fora do intervalo esperado (0-3)");
        } else {
            const predicao = await postEstudante(nome, rank_universidade, cgpa, dsa_score, coding_skills, internships);
            if (predicao) {
                if (predicao.resultado == 1){
                    alert("Previsão: Estudante será contratado!")
                } else {
                    alert("Previsão: Estudante não será contratado.")
                }
                limparForm()
                incluirViewEstudante(
                        predicao.nome, 
                        predicao.rank_universidade, 
                        predicao.cgpa, 
                        predicao.dsa_score, 
                        predicao.coding_skills, 
                        predicao.internships, 
                        predicao.resultado)
            } else {
                alert("Erro ao fazer a previsão.");
            }
        }        
    } else {
        alert("Preencha todos os campos para fazer a previsão.");
    }
}

function incluirViewEstudante(nome, rank_universidade, cgpa, dsa_score, coding_skills, internships, predicao) {
    let table = document.getElementById("table-estudantes");
    let row = table.insertRow();
    let mensagem_predicao;
    if (predicao == 1) {
        mensagem_predicao = "Sim";
    } else mensagem_predicao = "Não";

    let estudante = [nome, rank_universidade, cgpa, dsa_score, coding_skills, internships, mensagem_predicao];

    for (let i = 0; i < estudante.length; i++){
        let cell = row.insertCell(i);
        cell.textContent = estudante[i];
    }
}

function limparForm(){
    document.getElementById("nome").value = "";
    document.getElementById("rank_universidade").value = "";
    document.getElementById("cgpa").value = "";
    document.getElementById("dsa_score").value = "";
    document.getElementById("coding_skills").value = "";
    document.getElementById("internships").value = "";
}

function carrega_dados(){
    getListaEstudantes()
        .then(data=> {
            if ( data && data.estudantes ) {
                data.estudantes.forEach(estudante => incluirViewEstudante(
                    estudante.nome, 
                    estudante.rank_universidade, 
                    estudante.cgpa, 
                    estudante.dsa_score, 
                    estudante.coding_skills, 
                    estudante.internships, 
                    estudante.resultado));
            }
        })
        .catch(err => console.error('Erro:', err));
}

carrega_dados()
