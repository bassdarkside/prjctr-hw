CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(64) UNIQUE NOT NULL,
    email VARCHAR(64) UNIQUE NOT NULL,
    password VARCHAR(64) NOT NULL,
    phone VARCHAR(64) UNIQUE NOT NULL,
    description VARCHAR(300),
    created_at timestamp NOT NULL DEFAULT NOW(),
    updaded_at timestamp NOT NULL DEFAULT NOW()
);
CREATE TABLE IF NOT EXISTS rooms (
    id SERIAL PRIMARY KEY,
    owner_id INT references users(id),
    name VARCHAR(64) UNIQUE NOT NULL,
    address VARCHAR(64) UNIQUE NOT NULL,
    price DECIMAL NOT NULL,
    total_guests SMALLINT NOT NULL,
    bedrooms SMALLINT NOT NULL,
    has_wifi BOOLEAN NOT NULL,
    has_tv BOOLEAN NOT NULL,
    has_ac BOOLEAN NOT NULL,
    published_at timestamp NOT NULL DEFAULT NOW(),
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    created_at timestamp NOT NULL DEFAULT NOW(),
    updaded_at timestamp NOT NULL DEFAULT NOW()
);
CREATE TABLE IF NOT EXISTS reservations (
    id SERIAL PRIMARY KEY,
    user_id INT references users(id),
    room_id INT references rooms(id),
    price DECIMAL NOT NULL,
    check_in DATE NOT NULL,
    check_out DATE NOT NULL,
    total_price DECIMAL NOT NULL,
    created_at timestamp NOT NULL DEFAULT NOW(),
    updaded_at timestamp NOT NULL DEFAULT NOW()
);
CREATE TABLE IF NOT EXISTS payments (
    id SERIAL PRIMARY KEY,
    reservation_id INT NOT NULL references reservations(id),
    payment_ts timestamptz(3) NOT NULL DEFAULT NOW(),
    created_at timestamp NOT NULL DEFAULT NOW(),
    updaded_at timestamp NOT NULL DEFAULT NOW()
);
CREATE TABLE IF NOT EXISTS reviews (
    id SERIAL PRIMARY KEY,
    payment_id INT NOT NULL references payments(id),
    rating SMALLINT NOT NULL,
    comment VARCHAR(300) NOT NULL,
    created_at timestamp NOT NULL DEFAULT NOW(),
    updaded_at timestamp NOT NULL DEFAULT NOW()
);
INSERT INTO users (username, email, password, phone, description)
VALUES (
        'Leatha',
        'example@gmail.com',
        'qwerty123',
        '380663123467',
        'about Leatha'
    ),
    (
        'Chadd',
        'chadd15@gmail.com',
        'qwerty',
        '380995898495',
        'about Chadd'
    ),
    (
        'Nick',
        'nikkp5@gmail.com',
        'qwerty12345',
        '380975898495',
        'about Nick'
    ),
    (
        'Carrel',
        'carrel33@gmail.com',
        '23455432',
        '380635898495',
        'about Carrel'
    ),
    (
        'Boss',
        'boss@gmail.com',
        'zxcvbnASDFGH',
        '380935898495',
        'about Boss'
    ),
    (
        'Serhii',
        'serhii1988@gmail.com',
        'strong_pass',
        '380501248351',
        'Hello! My name is Serhii. I live in Kyiv.'
    ),
    (
        'Kharim',
        'jim_kharim@gmail.com',
        'mknj2113kde',
        '380671744341',
        'Hello! My name is Kharim. I live in Chop.'
    ),
    (
        'Katya',
        'katya@gmail.com',
        'my-pass',
        '3805743483315',
        'Hello! My name is Katya. I live in Bucha.'
    ),
    (
        'Helena',
        'heleha@gmail.com',
        'my_pass',
        '380501248559',
        'Hello! My name is Helena. I live in Kramatorsk.'
    ),
    (
        'Alex',
        'alex@gmail.com',
        'strong_pass',
        '380637243333',
        'Hello! My name is Alex. I live in Mariupol.'
    ),
    (
        'Budanov',
        'budanov_gru@gmail.com',
        'bayraktar',
        '380661111111',
        'Hello! My name is Kyrylo. I live in Sevavtopol.'
    );
INSERT INTO rooms (
        owner_id,
        name,
        address,
        price,
        total_guests,
        bedrooms,
        has_wifi,
        has_tv,
        has_ac,
        latitude,
        longitude
    )
VALUES (
        3,
        'Veranda 2',
        'Slavs"ke, Lvivs"ka oblast, Ukraine',
        54,
        2,
        1,
        True,
        True,
        True,
        48.848373730076645,
        23.44580418969173
    ),
    (
        1,
        '#1 Apiterapia na Roztoczu - Domek wypoczynkowy',
        'Kozaki, Lubelskie, Poland',
        57,
        3,
        2,
        True,
        True,
        False,
        39.848373730076645,
        22.44580418969173
    ),
    (
        4,
        'House',
        'Long str 112, New York',
        130,
        4,
        2,
        True,
        True,
        True,
        36.848373730076645,
        7.44580418969143
    ),
    (
        4,
        'Squad checkpoint',
        'Short str 99, New York',
        100,
        2,
        2,
        True,
        True,
        True,
        36.848373730074556,
        7.44580418964598
    ),
    (
        7,
        'Fazenda',
        'Yalta, Ukraine',
        45,
        2,
        1,
        True,
        False,
        False,
        56.848373730076645,
        50.44580418969173
    ),
    (
        5,
        'Industrial',
        'Tokke, Norway',
        250,
        5,
        3,
        True,
        True,
        True,
        32.848373730076645,
        24.44580418969173
    ),
    (
        5,
        'Port',
        'Tokke, Vestfold og Telemark, Norway',
        229,
        3,
        2,
        True,
        True,
        True,
        32.848373730076647,
        24.44580418969121
    ),
    (
        3,
        'Veranda 3',
        'Slavs"ke-3, Lvivs"ka oblast, Ukraine',
        100,
        2,
        1,
        True,
        True,
        True,
        48.848373730076649,
        23.44580418969176
    ),
    (
        3,
        'Veranda 4',
        'Slavs"ke-4, Lvivs"ka oblast, Ukraine',
        100,
        2,
        1,
        True,
        True,
        True,
        48.848373730076649,
        23.44580418969176
    ),
    (
        3,
        'Veranda 5',
        'Slavs"ke-5, Lvivs"ka oblast, Ukraine',
        100,
        2,
        1,
        True,
        True,
        True,
        48.848373730076649,
        23.44580418969176
    ),
    (
        3,
        'Veranda 6',
        'Slavs"ke-6, Lvivs"ka oblast, Ukraine',
        100,
        2,
        1,
        True,
        True,
        True,
        48.848373730076649,
        23.44580418969176
    );
INSERT INTO reservations (
        user_id,
        room_id,
        price,
        check_in,
        check_out,
        total_price
    )
VALUES (1, 2, 57, '2023-08-10', '2023-08-12', 114),
    (1, 2, 57, '2023-09-16', '2023-09-19', 171),
    (6, 1, 54, '2023-09-16', '2023-09-19', 162),
    (9, 3, 130, '2023-09-14', '2023-09-18', 520),
    (8, 5, 45, '2023-09-15', '2023-09-16', 45),
    (2, 10, 100, '2023-08-10', '2023-08-12', 100),
    (2, 11, 100, '2023-08-10', '2023-08-12', 100),
    (2, 12, 100, '2023-08-10', '2023-08-12', 100),
    (2, 13, 100, '2023-09-16', '2023-09-19', 200);
INSERT INTO payments (reservation_id)
VALUES (3),
    (1),
    (2);
INSERT INTO reviews (payment_id, rating, comment)
VALUES (1, 5, 'Relax and enjoy the nature.'),
    (2, 5, 'It was wonderful!!'),
    (3, 5, 'I recommend it!');
SELECT username,
    reservations.user_id
FROM reservations
    JOIN users ON users.id = reservations.user_id
GROUP BY username,
    user_id
ORDER BY COUNT(*) DESC
LIMIT 1;