CREATE TABLE eventos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    data DATE NOT NULL,
    local VARCHAR(150) NOT NULL,
    descricao TEXT,
    status VARCHAR(50) DEFAULT 'Agendado',

    CONSTRAINT chk_status 
    CHECK (status IN ('Agendado', 'Em andamento', 'Finalizado'))
);