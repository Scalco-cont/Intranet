from app import create_app
from app.extensions import db
from app.models import Administrador, Sistema, LinkUtil, Usuario, Comunicado

app = create_app()

# Cria tabelas e popula dados iniciais se o banco estiver vazio
with app.app_context():
    db.create_all()

    if not Administrador.query.filter_by(email='admin@empresa.com').first():
        admin = Administrador(nome='Administrador', email='admin@empresa.com')
        admin.set_senha('Admin@123')
        db.session.add(admin)

    if not Usuario.query.filter_by(email='editor@empresa.com').first():
        editor = Usuario(nome='Editor RH', email='editor@empresa.com', perfil='EDITOR')
        editor.set_senha('Editor@123')
        db.session.add(editor)

    db.session.flush()

    if Sistema.query.count() == 0:
        sistemas = [
            Sistema(nome='ERP', descricao='Sistema de gestao empresarial', icone='Building', url='https://erp.empresa.com', ordem_exibicao=1),
            Sistema(nome='Help Desk', descricao='Central de suporte e chamados', icone='Headset', url='https://helpdesk.empresa.com', ordem_exibicao=2),
            Sistema(nome='Financeiro', descricao='Controle financeiro e relatorios', icone='DollarSign', url='https://financeiro.empresa.com', ordem_exibicao=3),
            Sistema(nome='RH', descricao='Portal de Recursos Humanos', icone='Users', url='https://rh.empresa.com', ordem_exibicao=4),
            Sistema(nome='Monitoramento', descricao='Dashboards de infraestrutura', icone='Activity', url='https://monitoramento.empresa.com', ordem_exibicao=5),
            Sistema(nome='Controle de Tarefas', descricao='Gerenciamento de projetos', icone='CheckSquare', url='https://tarefas.empresa.com', ordem_exibicao=6),
            Sistema(nome='Sistema Fiscal', descricao='Gestao de notas fiscais', icone='FileText', url='https://fiscal.empresa.com', ordem_exibicao=7),
            Sistema(nome='CRM', descricao='Relacionamento com clientes', icone='PieChart', url='https://crm.empresa.com', ordem_exibicao=8),
        ]
        db.session.add_all(sistemas)

    if LinkUtil.query.count() == 0:
        links = [
            LinkUtil(nome='Receita Federal', descricao='Portal e-CAC e consultas', url='https://cav.receita.fazenda.gov.br', icone='Landmark', ordem_exibicao=1),
            LinkUtil(nome='Microsoft 365', descricao='Acesso ao pacote Office', url='https://www.office.com', icone='MonitorPlay', ordem_exibicao=2),
            LinkUtil(nome='WhatsApp Web', descricao='Comunicacao rapida via web', url='https://web.whatsapp.com', icone='MessageCircle', ordem_exibicao=3),
            LinkUtil(nome='Banco de Horas', descricao='Controle de ponto online', url='https://ponto.empresa.com', icone='Clock', ordem_exibicao=4),
            LinkUtil(nome='Wiki Interna', descricao='Base de conhecimento tecnica', url='https://wiki.empresa.com', icone='BookOpen', ordem_exibicao=5),
            LinkUtil(nome='Portal do Colaborador', descricao='Holerites e beneficios', url='https://colaborador.empresa.com', icone='UserCircle', ordem_exibicao=6),
        ]
        db.session.add_all(links)

    if Comunicado.query.count() == 0:
        editor = Usuario.query.filter_by(email='editor@empresa.com').first()
        comunicados = [
            Comunicado(
                titulo='Bem-vindo a nova Intranet!',
                conteudo='Estamos felizes em anunciar o lancamento da nossa nova Intranet Corporativa.',
                categoria='Geral',
                autor_id=editor.id if editor else None,
                fixado=True,
            ),
            Comunicado(
                titulo='Nova politica de ferias 2026',
                conteudo='Informamos que a nova politica de ferias ja esta disponivel para consulta no Portal do Colaborador.',
                categoria='RH',
                autor_id=editor.id if editor else None,
                fixado=False,
            ),
            Comunicado(
                titulo='Manutencao programada dos servidores',
                conteudo='Neste sabado, das 22h as 02h, realizaremos manutencao nos servidores.',
                categoria='TI',
                autor_id=editor.id if editor else None,
                fixado=False,
            ),
        ]
        db.session.add_all(comunicados)

    db.session.commit()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=app.config['DEBUG'])