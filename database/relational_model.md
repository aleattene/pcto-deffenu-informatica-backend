###4 Modello Relazionale

**Allenatori**  (**id_allenatore**, nome, cognome, cod_fiscale)

**Compensi** (**id_compenso**, data_erogazione, importo, _id_allenatore_)

**Atleti** (**id_atleta**, nome, cognome, data_nascita, luogo_nascita, cod_fiscale, _id_categoria_)

**StoricoAtletiAllenatori** (**id_storico**, _id_allenatore_, _id_atleta_, data_inizio, data_fine)

**Categorie** (**id_categoria**, codice, descrizione)

**CertificazioniSanitarie** (**id_certificazione**, data_emissione. data_scadenza, _id_atleta_, _id_medico_)

**Medici** (**id_medico**, p_iva, nome, cognome)
