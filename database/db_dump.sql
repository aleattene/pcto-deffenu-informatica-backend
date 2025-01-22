CREATE TABLE Allenatori ( 
  id_allenatore INT PRIMARY KEY,
  nome VARCHAR (255) NOT NULL,
  cognome VARCHAR (255) NOT NULL,
  cod_fiscale VARCHAR (16) NOT NULL UNIQUE
);


CREATE TABLE Compensi ( 
  id_compenso INT PRIMARY KEY,
  data_erogazione DATE NOT NULL,
  importo DECIMAL (10,2) NOT NULL,
  id_allenatore INT NOT NULL,
  FOREIGN KEY (id_allenatore) REFERENCES Allenatori (id_allenatore)                         
);

CREATE TABLE Atleti (
  id_atleta INT PRIMARY KEY,
  nome VARCHAR (255) NOT NULL,
  cognome VARCHAR (255) NOT NULL,
  data_nascita DATE NOT NULL,
  luogo_nascita VARCHAR (255) NOT NULL,
  cod_fiscale VARCHAR (16) NOT NULL UNIQUE,
  id_categoria INT NOT NULL,
  FOREIGN KEY (id_categoria) REFERENCES Categorie (id_categoria)
);

CREATE TABLE StoricoAtletiAllenatori (
  id_storico INT PRIMARY KEY,
  id_allenatore INT NOT NULL,
  id_atleta INT NOT NULL,
  data_inizio DATE NOT NULL,
  data_fine DATE NOT NULL,
  FOREIGN KEY (id_allenatore) REFERENCES Allenatori (id_allenatori),
  FOREIGN KEY (id_atleta) REFERENCES Atleti (id_atleta)
 );
  
 CREATE TABLE Categorie (
   id_categoria INT PRIMARY KEY,
   codice INT NOT NULL,
   descrizione VARCHAR (255) NOT NULL
 );
 
 CREATE TABLE CertificazioniSanitarie (
   id_certificazione INT PRIMARY KEY,
   data_emissione DATE NOT NULL,
   data_scadenza DATE NOT NULL,
   id_atleta INT NOT NULL,
   id_medico INT NOT NULL,
   FOREIGN KEY (id_atleta) REFERENCES Atleti (id_atleta),
   FOREIGN KEY (id_medico) REFERENCES Medici (id_medico)
 );
 
 CREATE TABLE Medici (
   id_medico INT PRIMARY KEY,
   p_iva VARCHAR (11) NOT NULL,
   nome VARCHAR (255) NOT NULL,
   cognome VARCHAR (255) NOT NULL
 );
   