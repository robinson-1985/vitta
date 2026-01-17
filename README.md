# 🏥 VITTA – Sistema de Atendimento em Saúde
🚧 Projeto em desenvolvimento

Sistema web desenvolvido com Python e Django para gestão de atendimentos em saúde,
voltado a clínicas, hospitais, ambulatórios e serviços de Home Care.

Projeto desenvolvido como laboratório prático para estudo de arquitetura backend,
modelagem de dados e problemas reais da área da saúde.

🔧 Stack: Python • Django • HTML • CSS • SQLite

## 🚀 Status do Projeto

O VITTA encontra-se em desenvolvimento ativo.

Funcionalidades já implementadas:
- Cadastro de pacientes
- Agendamento de consultas
- Agenda diária com filtro por data
- Prontuário vinculado à consulta
- Autenticação de usuários

Funcionalidades em evolução:
- Permissões por perfil
- Melhorias de UX
- Adequação progressiva à LGPD

## ▶️ Como executar localmente

```bash
git clone https://github.com/robinson-1985/vitta
cd vitta
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
