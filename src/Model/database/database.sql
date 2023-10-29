CREATE DATABASE hospitaldb;

CREATE TABLE medicos(
    id int PRIMARY KEY AUTO_INCREMENT,
    nome varchar(80) NOT NULL,
    email varchar(100) NOT NULL,
    telefone char(19) NOT NULL,
    cpf char(20) NOT NULL,
    rg char(20) NOT NULL,
    formacao varchar(90) NOT NULL,
    setor varchar(80) NOT NULL
);

CREATE TABLE pacientes(
    id int PRIMARY KEY AUTO_INCREMENT,
    nome varchar(100) NOT NULL,
    email varchar(100) NOT NULL,
    telefone char(19) NOT NULL,
    cpf char(20) NOT NULL,
    rg char(20) NOT NULL
);

CREATE TABLE consultas(
    id int PRIMARY KEY AUTO_INCREMENT,
    tipo_consulta varchar(80) NOT NULL,
    dataConsulta char(10) NOT NULL,
    horario char(5) NOT NULL,
    endereco varchar(50) NOT NULL,
    id_medico int NOT NULL,
    FOREIGN KEY (`id_medico`) REFERENCES `medicos` (`id`),
    FOREIGN KEY (`id_paciente`) REFERENCES `pacientes` (`id`)
);