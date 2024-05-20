-- Tabla "cajero"
CREATE TABLE IF NOT EXISTS cajero (
  id_cajero SERIAL PRIMARY KEY,
  saldo DECIMAL(10,2)
);

-- Tabla "cliente"
CREATE TABLE IF NOT EXISTS cliente (
  id_cliente SERIAL PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  apellido VARCHAR(50) NOT NULL
);

-- Tabla "servicios"
CREATE TABLE IF NOT EXISTS servicios (
  id_servicio SERIAL PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL
);

-- Tabla "cuenta"
CREATE TABLE IF NOT EXISTS cuenta (
  num_cuenta SERIAL PRIMARY KEY,
  num_debito VARCHAR(20),
  id_cliente INT,
  saldo DECIMAL(10,2),
  vencimiento_debito DATE,
  nip_debito VARCHAR(4),
  FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
);

-- Tabla "pago_servicio"
CREATE TABLE IF NOT EXISTS pago_servicio (
  id_pago SERIAL PRIMARY KEY,
  id_servicio INT,
  num_cuenta INT,
  monto DECIMAL(10,2),
  FOREIGN KEY (id_servicio) REFERENCES servicios(id_servicio),
  FOREIGN KEY (num_cuenta) REFERENCES cuenta(num_cuenta)
);

-- Tabla "tarjeta_cto"
CREATE TABLE IF NOT EXISTS tarjeta_cto (
  num_tarjeta SERIAL PRIMARY KEY,
  num_cuenta INT,
  nip VARCHAR(4),
  saldo_actual DECIMAL(10,2),
  a_pagar DECIMAL(10,2),
  fecha_vencimiento DATE,
  FOREIGN KEY (num_cuenta) REFERENCES cuenta(num_cuenta)
);

-- Tabla "tipomovimiento"
CREATE TABLE IF NOT EXISTS tipomovimiento (
  id_tipoMovimiento SERIAL PRIMARY KEY,
  descripcion VARCHAR(50) NOT NULL
);

-- Tabla "transacciones"
CREATE TABLE IF NOT EXISTS transacciones (
  id_transaccion SERIAL PRIMARY KEY,
  num_cuenta INT,
  id_cajero INT,
  id_tipoMovimiento INT,
  fecha_movimiento TIMESTAMP,
  concepto VARCHAR(255),
  FOREIGN KEY (num_cuenta) REFERENCES cuenta(num_cuenta),
  FOREIGN KEY (id_cajero) REFERENCES cajero(id_cajero),
  FOREIGN KEY (id_tipoMovimiento) REFERENCES tipomovimiento(id_tipoMovimiento)
);
