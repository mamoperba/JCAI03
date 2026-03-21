create database db_gudang;
use db_gudang;
Create table sparepart (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama_part VARCHAR(100),
    kategori VARCHAR(50),
    merk VARCHAR(50),
    harga INT,
    stok INT,
    tanggal_masuk DATE
);

show tables;
select * from sparepart;
INSERT INTO sparepart (nama_part, kategori, merk, harga, stok, tanggal_masuk) VALUES
('Oli Mesin 5W-30', 'Mesin', 'Shell', 120000, 50, '2026-01-10'),
('Kampas Rem Depan', 'Kaki-kaki', 'Brembo', 350000, 30, '2026-01-12'),
('Filter Udara', 'Mesin', 'Toyota', 80000, 40, '2026-01-15'),
('Aki Mobil 12V', 'Kelistrikan', 'GS Astra', 950000, 20, '2026-01-18'),
('Busi Iridium', 'Mesin', 'NGK', 45000, 100, '2026-01-20'),
('Radiator Coolant', 'Pendingin', 'Prestone', 70000, 60, '2026-01-22'),
('Lampu LED Headlamp', 'Kelistrikan', 'Philips', 250000, 25, '2026-01-25'),
('Shockbreaker Belakang', 'Kaki-kaki', 'KYB', 600000, 15, '2026-01-28'),
('Filter Oli', 'Mesin', 'Bosch', 60000, 70, '2026-02-01'),
('Kopling Set', 'Transmisi', 'Exedy', 1200000, 10, '2026-02-05');


