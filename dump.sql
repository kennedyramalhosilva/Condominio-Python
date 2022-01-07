CREATE TABLE IF NOT EXISTS condominio (
idCondominio INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
cnpj TEXT, 
nome TEXT
);

  CREATE TABLE IF NOT EXISTS apartamento(
  idApartamento INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
  bloco TEXT,
numero INTEGER,
idCondominio INTEGER,
FOREIGN KEY (idCondominio) REFERENCES condominio(idCondominio)
);

CREATE TABLE IF NOT EXISTS visitante(
idVisitante INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
nome TEXT, 
rg TEXT, 
telefone TEXT,
idApartamento INTEGER,
FOREIGN KEY (idApartamento) REFERENCES apartamento(idApartamento)
);

CREATE TABLE IF NOT EXISTS morador(
idMorador INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
nome TEXT,
rg TEXT,
telefone TEXT,
idApartamento INTEGER,
FOREIGN KEY (idApartamento) REFERENCES apartamento(idApartamento)
);

CREATE TABLE IF NOT EXISTS veiculo
(idVeiculo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
placa TEXT, 
marca TEXT,
modelo TEXT,
cor TEXT,
idMorador INTEGER,
FOREIGN KEY (idMorador) REFERENCES morador(idMorador)
);

CREATE TABLE IF NOT EXISTS funcionario(
idFuncionario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
nome TEXT,
rg TEXT, 
telefone TEXT,
idCondominio INTEGER,
FOREIGN KEY (idCondominio) REFERENCES condominio(idCondominio
);