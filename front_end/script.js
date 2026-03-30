const host_api = window.HOST_API || "http://127.0.0.1:5000/";

async function postEstudante(rank_universidade, cgpa, dsa_score, coding_skills, internships) {
    let url = host_api + "estudante"
    const response = await fetch(url, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({rank_universidade: rank_universidade, 
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

async function estimarContratacao() {
    let rank_universidade = document.getElementById("rank_universidade").value;
    let cgpa = document.getElementById("cgpa").value;
    let dsa_score = document.getElementById("dsa_score").value;
    let coding_skills = document.getElementById("coding_skills").value;
    let internships = document.getElementById("internships").value;
    
    
    if (rank_universidade && cgpa && dsa_score && coding_skills && internships){
        const predicao = await postEstudante(rank_universidade, cgpa, dsa_score, coding_skills, internships);
        if (predicao) {
            if (predicao.resultado == 1){
                alert("Predição: Aluno será contratado!")
            } else {
                alert("Predição: Aluno não será contratado.")
            }            
        } else {
            alert("Erro ao fazer a predição.");
        }
        
    } else {
        alert("Preencha todos os campos para fazer a predição.");
    }
}