-- Inserciones para la tabla "cajero"
INSERT INTO cajero (saldo) VALUES
(1000.00),
(1500.50),
(2000.75),
(2500.00),
(3000.25),
(3500.50),
(4000.75),
(4500.00),
(5000.25),
(5500.50);

-- Inserciones para la tabla "cliente"
INSERT INTO cliente (nombre, apellido) VALUES
('Juan', 'Pérez'),
('Ana', 'Gómez'),
('Luis', 'Martínez'),
('María', 'Rodríguez'),
('Carlos', 'López'),
('Lucía', 'Fernández'),
('José', 'García'),
('Elena', 'Sánchez'),
('Pedro', 'Martín'),
('Sofía', 'Jiménez');

-- Inserciones para la tabla "servicios"
INSERT INTO servicios (nombre) VALUES
('Electricidad'),
('Agua'),
('Internet'),
('Gas'),
('Telefonía'),
('Televisión por cable'),
('Streaming'),
('Alarma'),
('Seguridad'),
('Limpieza');

-- Inserciones para la tabla "cuenta"
INSERT INTO cuenta (num_debito, id_cliente, saldo, vencimiento_debito, nip_debito) VALUES
('1111-1111-1111-1111', 1, 500.00, '2025-12-31', '1234'),
('2222-2222-2222-2222', 2, 600.00, '2025-11-30', '2345'),
('3333-3333-3333-3333', 3, 700.00, '2025-10-31', '3456'),
('4444-4444-4444-4444', 4, 800.00, '2025-09-30', '4567'),
('5555-5555-5555-5555', 5, 900.00, '2025-08-31', '5678'),
('6666-6666-6666-6666', 6, 1000.00, '2025-07-31', '6789'),
('7777-7777-7777-7777', 7, 1100.00, '2025-06-30', '7890'),
('8888-8888-8888-8888', 8, 1200.00, '2025-05-31', '8901'),
('9999-9999-9999-9999', 9, 1300.00, '2025-04-30', '9012'),
('0000-0000-0000-0000', 10, 1400.00, '2025-03-31', '0123');

-- Inserciones para la tabla "pago_servicio"
INSERT INTO pago_servicio (id_servicio, num_cuenta, monto) VALUES
(1, 1, 50.00),
(2, 2, 60.00),
(3, 3, 70.00),
(4, 4, 80.00),
(5, 5, 90.00),
(6, 6, 100.00),
(7, 7, 110.00),
(8, 8, 120.00),
(9, 9, 130.00),
(10, 10, 140.00);

-- Inserciones para la tabla "tarjeta_cto"
INSERT INTO tarjeta_cto (num_cuenta, nip, saldo_actual, a_pagar, fecha_vencimiento) VALUES
(1, '1234', 300.00, 50.00, '2025-12-31'),
(2, '2345', 400.00, 60.00, '2025-11-30'),
(3, '3456', 500.00, 70.00, '2025-10-31'),
(4, '4567', 600.00, 80.00, '2025-09-30'),
(5, '5678', 700.00, 90.00, '2025-08-31'),
(6, '6789', 800.00, 100.00, '2025-07-31'),
(7, '7890', 900.00, 110.00, '2025-06-30'),
(8, '8901', 1000.00, 120.00, '2025-05-31'),
(9, '9012', 1100.00, 130.00, '2025-04-30'),
(10, '0123', 1200.00, 140.00, '2025-03-31');

-- Inserciones para la tabla "tipomovimiento"
INSERT INTO tipomovimiento (descripcion) VALUES
('Depósito'),
('Retiro'),
('Transferencia'),
('Pago de servicio'),
('Compra'),
('Pago de tarjeta'),
('Interés generado'),
('Interés cobrado'),
('Comisión'),
('Devolución');

-- Inserciones para la tabla "transacciones"
INSERT INTO transacciones (num_cuenta, id_cajero, id_tipoMovimiento, fecha_movimiento, concepto) VALUES
(1, 1, 1, '2024-01-01 10:00:00', 'Depósito inicial'),
(2, 2, 2, '2024-01-02 11:00:00', 'Retiro en cajero'),
(3, 3, 3, '2024-01-03 12:00:00', 'Transferencia a otra cuenta'),
(4, 4, 4, '2024-01-04 13:00:00', 'Pago de factura de electricidad'),
(5, 5, 5, '2024-01-05 14:00:00', 'Compra en tienda'),
(6, 6, 6, '2024-01-06 15:00:00', 'Pago de tarjeta de crédito'),
(7, 7, 7, '2024-01-07 16:00:00', 'Interés generado en cuenta'),
(8, 8, 8, '2024-01-08 17:00:00', 'Interés cobrado por préstamo'),
(9, 9, 9, '2024-01-09 18:00:00', 'Comisión por transferencia'),
(10, 10, 10, '2024-01-10 19:00:00', 'Devolución de compra');

