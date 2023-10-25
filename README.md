# Sistema de Hospital 🏥🩺

Este projeto tem como objetivo aplicar conhecimentos sólidos em desenvolvimento de software, modelagem de sistemas e gerenciamento de bancos de dados em um ambiente de extrema relevância - a área da saúde. O foco principal é o desenvolvimento de um Sistema de Gestão Hospitalar que permitirá o registro de pacientes, médicos, agendamento de consultas e a visualização das consultas agendadas.

## 📋 Pré-requisitos
De que coisas você precisa para instalar o software e como instalá-lo?

1. Python: Certifique-se de ter o Python instalado em sua máquina. Se você ainda não o tem, pode fazer o <a href="https://www.python.org/downloads/" download>Download Aqui</a>..

2. MySQL: O sistema requer um servidor MySQL. Você pode fazer o download do MySQL <a href="https://www.mysql.com/downloads/" download>Download Aqui</a>.

3. Instalação da Biblioteca Tkinter: Para a interface gráfica, você precisará da biblioteca Tkinter. Você pode instalá-la facilmente utilizando o comando a seguir:
Windows:

3.1. Pressione as teclas Windows + R.

3.2. Digite cmd e pressione Enter para abrir o prompt de comando.

3.3. Cole o seguinte comando e pressione Enter para instalar o Tkinter:

```plaintext
pip install tkinter
```
Com o cmd (Terminal) aberto execute outro comando : 

```plaintext
pip install mysql-connector-python
```
## Configurando Banco de Dados

Antes de usar o sistema, é necessário configurar o banco de dados. Siga as etapas abaixo:

### Passo 1: Crie o Banco de Dados
Abra o MySQL e execute o seguinte comando para criar o banco de dados HospitalDB:

```plaintext
create database HospitalDB;
```

### Passo 2: Selecione o Banco de Dados
Depois de criar o banco de dados, selecione-o usando o comando USE:

```plaintext
use HospitalDB;
```

### Passo 3: Criar Tabelas
Depois de selecionar o banco de dados, crie as tabelas:

Tabela de Pacientes
```plaintext
    create table pacientes(
	  id int primary key auto_increment,
    nome varchar(100) not null,
    email varchar(100) not null,
    telefone char(19) not null,
    cpf char(20) not null,
    rg char(20) not null
);
```

<hr/>

Tabela de Medicos
```plaintext
    create table medicos(
  	id int primary key auto_increment,
    nome varchar(80) not null,
    email varchar(100) not null,
    telefone char(19) not null,
    cpf char(20) not null,
    rg char(20) not null,
    formacao varchar(90) not null,
    setor varchar(80) not null
);
```

<hr/>

Tabela de Consultas
```plaintext
    create table consultas(
	  id int primary key auto_increment,
    tipo_consulta varchar(80) not null, 
    dataConsulta char(10) not null,
    horario char(5) not null, 
    endereco varchar(50) not null,
    id_medico int not null,
    id_paciente int not null,
    foreign key(id_medico) references medicos(id),
    foreign key(id_paciente) references pacientes(id)
);
```







