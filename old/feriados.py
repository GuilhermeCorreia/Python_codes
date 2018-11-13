import datetime


def lista():
    feriados = (
        datetime.date(2000, 5, 1),
        datetime.date(2000, 12, 29),
        datetime.date(2001, 1, 1),
        datetime.date(2001, 2, 26),
        datetime.date(2001, 2, 27),
        datetime.date(2001, 4, 21),
        datetime.date(2001, 5, 1),
        datetime.date(2001, 6, 14),
        datetime.date(2001, 9, 7),
        datetime.date(2001, 11, 2),
        datetime.date(2001, 11, 15),
        datetime.date(2001, 12, 25),
        datetime.date(2001, 12, 31),
        datetime.date(2002, 1, 1),
        datetime.date(2002, 2, 11),
        datetime.date(2002, 2, 12),
        datetime.date(2002, 3, 29),
        datetime.date(2002, 4, 21),
        datetime.date(2002, 5, 1),
        datetime.date(2002, 5, 30),
        datetime.date(2002, 9, 7),
        datetime.date(2002, 10, 12),
        datetime.date(2002, 11, 2),
        datetime.date(2002, 12, 25),
        datetime.date(2002, 12, 31),
        datetime.date(2003, 1, 1),
        datetime.date(2003, 3, 3),
        datetime.date(2003, 3, 4),
        datetime.date(2003, 4, 21),
        datetime.date(2003, 5, 1),
        datetime.date(2003, 6, 19),
        datetime.date(2003, 7, 9),
        datetime.date(2003, 9, 7),
        datetime.date(2003, 11, 2),
        datetime.date(2003, 12, 25),
        datetime.date(2003, 12, 31),
        datetime.date(2004, 1, 1),
        datetime.date(2004, 2, 23),
        datetime.date(2004, 4, 9),
        datetime.date(2004, 4, 21),
        datetime.date(2004, 5, 1),
        datetime.date(2004, 6, 10),
        datetime.date(2004, 10, 12),
        datetime.date(2004, 9, 7),
        datetime.date(2004, 11, 2),
        datetime.date(2004, 11, 15),
        datetime.date(2004, 12, 25),
        datetime.date(2004, 12, 31),
        datetime.date(2005, 1, 1),
        datetime.date(2005, 2, 7),
        datetime.date(2005, 2, 8),
        datetime.date(2005, 3, 25),
        datetime.date(2005, 4, 21),
        datetime.date(2005, 5, 1),
        datetime.date(2005, 5, 26),
        datetime.date(2005, 9, 7),
        datetime.date(2005, 10, 12),
        datetime.date(2005, 11, 2),
        datetime.date(2005, 11, 15),
        datetime.date(2005, 12, 25),
        datetime.date(2005, 12, 30),
        datetime.date(2005, 12, 31),
        datetime.date(2006, 1, 1),
        datetime.date(2006, 2, 27),
        datetime.date(2006, 2, 28),
        datetime.date(2006, 4, 14),
        datetime.date(2006, 4, 21),
        datetime.date(2006, 5, 1),
        datetime.date(2006, 6, 15),
        datetime.date(2006, 9, 7),
        datetime.date(2006, 10, 12),
        datetime.date(2006, 11, 2),
        datetime.date(2006, 11, 15),
        datetime.date(2006, 12, 25),
        datetime.date(2006, 12, 29),
        datetime.date(2006, 12, 30),
        datetime.date(2006, 12, 31),
        datetime.date(2007, 1, 1),
        datetime.date(2007, 2, 19),
        datetime.date(2007, 2, 20),
        datetime.date(2007, 4, 6),
        datetime.date(2007, 4, 21),
        datetime.date(2007, 5, 1),
        datetime.date(2007, 6, 7),
        datetime.date(2007, 9, 7),
        datetime.date(2007, 10, 12),
        datetime.date(2007, 11, 2),
        datetime.date(2007, 11, 15),
        datetime.date(2007, 12, 25),
        datetime.date(2007, 12, 31),
        datetime.date(2008, 1, 1),
        datetime.date(2008, 2, 4),
        datetime.date(2008, 2, 5),
        datetime.date(2008, 3, 21),
        datetime.date(2008, 4, 21),
        datetime.date(2008, 5, 1),
        datetime.date(2008, 5, 22),
        datetime.date(2008, 9, 7),
        datetime.date(2008, 10, 12),
        datetime.date(2008, 11, 2),
        datetime.date(2008, 11, 15),
        datetime.date(2008, 12, 25),
        datetime.date(2008, 12, 31),
        datetime.date(2009, 1, 1),
        datetime.date(2009, 2, 23),
        datetime.date(2009, 2, 24),
        datetime.date(2009, 4, 10),
        datetime.date(2009, 4, 21),
        datetime.date(2009, 5, 1),
        datetime.date(2009, 6, 11),
        datetime.date(2009, 9, 7),
        datetime.date(2009, 10, 12),
        datetime.date(2009, 11, 2),
        datetime.date(2009, 11, 15),
        datetime.date(2009, 12, 25),
        datetime.date(2009, 12, 31),
        datetime.date(2010, 1, 1),
        datetime.date(2010, 2, 15),
        datetime.date(2010, 2, 16),
        datetime.date(2010, 4, 2),
        datetime.date(2010, 4, 21),
        datetime.date(2010, 5, 1),
        datetime.date(2010, 6, 3),
        datetime.date(2010, 9, 7),
        datetime.date(2010, 10, 12),
        datetime.date(2010, 11, 2),
        datetime.date(2010, 11, 15),
        datetime.date(2010, 12, 25),
        datetime.date(2010, 12, 31),
        datetime.date(2011, 1, 1),
        datetime.date(2011, 3, 7),
        datetime.date(2011, 3, 8),
        datetime.date(2011, 4, 21),
        datetime.date(2011, 4, 22),
        datetime.date(2011, 5, 1),
        datetime.date(2011, 6, 23),
        datetime.date(2011, 9, 7),
        datetime.date(2011, 10, 12),
        datetime.date(2011, 11, 2),
        datetime.date(2011, 11, 15),
        datetime.date(2011, 12, 25),
        datetime.date(2011, 12, 30),
        datetime.date(2011, 12, 31),
        datetime.date(2012, 1, 1),
        datetime.date(2012, 2, 20),
        datetime.date(2012, 2, 21),
        datetime.date(2012, 4, 6),
        datetime.date(2012, 4, 21),
        datetime.date(2012, 5, 1),
        datetime.date(2012, 6, 7),
        datetime.date(2012, 9, 7),
        datetime.date(2012, 10, 12),
        datetime.date(2012, 11, 2),
        datetime.date(2012, 11, 15),
        datetime.date(2012, 12, 25),
        datetime.date(2012, 12, 31),
        datetime.date(2013, 1, 1),
        datetime.date(2013, 2, 11),
        datetime.date(2013, 2, 12),
        datetime.date(2013, 3, 29),
        datetime.date(2013, 4, 21),
        datetime.date(2013, 5, 1),
        datetime.date(2013, 5, 30),
        datetime.date(2013, 9, 7),
        datetime.date(2013, 10, 12),
        datetime.date(2013, 11, 2),
        datetime.date(2013, 11, 15),
        datetime.date(2013, 12, 25),
        datetime.date(2013, 12, 30),
        datetime.date(2013, 12, 31),
        datetime.date(2014, 1, 1),
        datetime.date(2014, 3, 3),
        datetime.date(2014, 3, 4),
        datetime.date(2014, 4, 18),
        datetime.date(2014, 4, 21),
        datetime.date(2014, 5, 1),
        datetime.date(2014, 6, 19),
        datetime.date(2014, 9, 7),
        datetime.date(2014, 10, 12),
        datetime.date(2014, 11, 2),
        datetime.date(2014, 11, 15),
        datetime.date(2014, 12, 25),
        datetime.date(2014, 12, 31),
        datetime.date(2015, 1, 1),
        datetime.date(2015, 2, 16),
        datetime.date(2015, 2, 17),
        datetime.date(2015, 4, 3),
        datetime.date(2015, 4, 21),
        datetime.date(2015, 5, 1),
        datetime.date(2015, 6, 4),
        datetime.date(2015, 9, 7),
        datetime.date(2015, 10, 12),
        datetime.date(2015, 11, 2),
        datetime.date(2015, 11, 15),
        datetime.date(2015, 12, 25),
        datetime.date(2015, 12, 31),
        datetime.date(2016, 1, 1),
        datetime.date(2016, 2, 8),
        datetime.date(2016, 2, 9),
        datetime.date(2016, 3, 25),
        datetime.date(2016, 4, 21),
        datetime.date(2016, 5, 1),
        datetime.date(2016, 5, 26),
        datetime.date(2016, 9, 7),
        datetime.date(2016, 10, 12),
        datetime.date(2016, 11, 2),
        datetime.date(2016, 11, 15),
        datetime.date(2016, 12, 25),
        datetime.date(2016, 12, 30),
        datetime.date(2016, 12, 31),
        datetime.date(2017, 1, 1),
        datetime.date(2017, 2, 27),
        datetime.date(2017, 2, 28),
        datetime.date(2017, 4, 14),
        datetime.date(2017, 4, 21),
        datetime.date(2017, 5, 1),
        datetime.date(2017, 6, 15),
        datetime.date(2017, 9, 7),
        datetime.date(2017, 10, 12),
        datetime.date(2017, 11, 2),
        datetime.date(2017, 11, 15),
        datetime.date(2017, 12, 25),
        datetime.date(2017, 12, 31),
        datetime.date(2018, 1, 1),
        datetime.date(2018, 2, 12),
        datetime.date(2018, 2, 13),
        datetime.date(2018, 3, 30),
        datetime.date(2018, 4, 21),
        datetime.date(2018, 5, 1),
        datetime.date(2018, 5, 31),
        datetime.date(2018, 9, 7),
        datetime.date(2018, 10, 12),
        datetime.date(2018, 11, 2),
        datetime.date(2018, 11, 15),
        datetime.date(2018, 12, 25),
        datetime.date(2019, 1, 1),
        datetime.date(2019, 3, 4),
        datetime.date(2019, 3, 5),
        datetime.date(2019, 4, 19),
        datetime.date(2019, 4, 21),
        datetime.date(2019, 5, 1),
        datetime.date(2019, 6, 20),
        datetime.date(2019, 9, 7),
        datetime.date(2019, 10, 12),
        datetime.date(2019, 11, 2),
        datetime.date(2019, 11, 15),
        datetime.date(2019, 12, 25),
        datetime.date(2020, 1, 1),
        datetime.date(2020, 2, 24),
        datetime.date(2020, 2, 25),
        datetime.date(2020, 4, 10),
        datetime.date(2020, 4, 21),
        datetime.date(2020, 5, 1),
        datetime.date(2020, 6, 11),
        datetime.date(2020, 9, 7),
        datetime.date(2020, 10, 12),
        datetime.date(2020, 11, 2),
        datetime.date(2020, 11, 15),
        datetime.date(2020, 12, 25),
        datetime.date(2021, 1, 1),
        datetime.date(2021, 2, 15),
        datetime.date(2021, 2, 16),
        datetime.date(2021, 4, 2),
        datetime.date(2021, 4, 21),
        datetime.date(2021, 5, 1),
        datetime.date(2021, 6, 3),
        datetime.date(2021, 9, 7),
        datetime.date(2021, 10, 12),
        datetime.date(2021, 11, 2),
        datetime.date(2021, 11, 15),
        datetime.date(2021, 12, 25),
        datetime.date(2022, 1, 1),
        datetime.date(2022, 2, 28),
        datetime.date(2022, 3, 1),
        datetime.date(2022, 4, 15),
        datetime.date(2022, 4, 21),
        datetime.date(2022, 5, 1),
        datetime.date(2022, 6, 16),
        datetime.date(2022, 9, 7),
        datetime.date(2022, 10, 12),
        datetime.date(2022, 11, 2),
        datetime.date(2022, 11, 15),
        datetime.date(2022, 12, 25),
        datetime.date(2023, 1, 1),
        datetime.date(2023, 2, 20),
        datetime.date(2023, 2, 21),
        datetime.date(2023, 4, 7),
        datetime.date(2023, 4, 21),
        datetime.date(2023, 5, 1),
        datetime.date(2023, 6, 8),
        datetime.date(2023, 9, 7),
        datetime.date(2023, 10, 12),
        datetime.date(2023, 11, 2),
        datetime.date(2023, 11, 15),
        datetime.date(2023, 12, 25),
        datetime.date(2024, 1, 1),
        datetime.date(2024, 2, 12),
        datetime.date(2024, 2, 13),
        datetime.date(2024, 3, 29),
        datetime.date(2024, 4, 21),
        datetime.date(2024, 5, 1),
        datetime.date(2024, 5, 30),
        datetime.date(2024, 9, 7),
        datetime.date(2024, 10, 12),
        datetime.date(2024, 11, 2),
        datetime.date(2024, 11, 15),
        datetime.date(2024, 12, 25),
        datetime.date(2025, 1, 1),
        datetime.date(2025, 3, 3),
        datetime.date(2025, 3, 4),
        datetime.date(2025, 4, 18),
        datetime.date(2025, 4, 21),
        datetime.date(2025, 5, 1),
        datetime.date(2025, 6, 19),
        datetime.date(2025, 9, 7),
        datetime.date(2025, 10, 12),
        datetime.date(2025, 11, 2),
        datetime.date(2025, 11, 15),
        datetime.date(2025, 12, 25),
        datetime.date(2026, 1, 1),
        datetime.date(2026, 2, 16),
        datetime.date(2026, 2, 17),
        datetime.date(2026, 4, 3),
        datetime.date(2026, 4, 21),
        datetime.date(2026, 5, 1),
        datetime.date(2026, 6, 4),
        datetime.date(2026, 9, 7),
        datetime.date(2026, 10, 12),
        datetime.date(2026, 11, 2),
        datetime.date(2026, 11, 15),
        datetime.date(2026, 12, 25),
        datetime.date(2027, 1, 1),
        datetime.date(2027, 2, 8),
        datetime.date(2027, 2, 9),
        datetime.date(2027, 3, 26),
        datetime.date(2027, 4, 21),
        datetime.date(2027, 5, 1),
        datetime.date(2027, 5, 27),
        datetime.date(2027, 9, 7),
        datetime.date(2027, 10, 12),
        datetime.date(2027, 11, 2),
        datetime.date(2027, 11, 15),
        datetime.date(2027, 12, 25),
        datetime.date(2028, 1, 1),
        datetime.date(2028, 2, 28),
        datetime.date(2028, 2, 29),
        datetime.date(2028, 4, 14),
        datetime.date(2028, 4, 21),
        datetime.date(2028, 5, 1),
        datetime.date(2028, 6, 15),
        datetime.date(2028, 9, 7),
        datetime.date(2028, 10, 12),
        datetime.date(2028, 11, 2),
        datetime.date(2028, 11, 15),
        datetime.date(2028, 12, 25),
        datetime.date(2029, 1, 1),
        datetime.date(2029, 2, 12),
        datetime.date(2029, 2, 13),
        datetime.date(2029, 3, 30),
        datetime.date(2029, 4, 21),
        datetime.date(2029, 5, 1),
        datetime.date(2029, 5, 31),
        datetime.date(2029, 9, 7),
        datetime.date(2029, 10, 12),
        datetime.date(2029, 11, 2),
        datetime.date(2029, 11, 15),
        datetime.date(2029, 12, 25),
        datetime.date(2030, 1, 1),
        datetime.date(2030, 3, 4),
        datetime.date(2030, 3, 5),
        datetime.date(2030, 4, 19),
        datetime.date(2030, 4, 21),
        datetime.date(2030, 5, 1),
        datetime.date(2030, 6, 20),
        datetime.date(2030, 9, 7),
        datetime.date(2030, 10, 12),
        datetime.date(2030, 11, 2),
        datetime.date(2030, 11, 15),
        datetime.date(2030, 12, 25),
        datetime.date(2031, 1, 1),
        datetime.date(2031, 2, 24),
        datetime.date(2031, 2, 25),
        datetime.date(2031, 4, 11),
        datetime.date(2031, 4, 21),
        datetime.date(2031, 5, 1),
        datetime.date(2031, 6, 12),
        datetime.date(2031, 9, 7),
        datetime.date(2031, 10, 12),
        datetime.date(2031, 11, 2),
        datetime.date(2031, 11, 15),
        datetime.date(2031, 12, 25),
        datetime.date(2032, 1, 1),
        datetime.date(2032, 2, 9),
        datetime.date(2032, 2, 10),
        datetime.date(2032, 3, 26),
        datetime.date(2032, 4, 21),
        datetime.date(2032, 5, 27),
        datetime.date(2032, 9, 7),
        datetime.date(2032, 10, 12),
        datetime.date(2032, 11, 2),
        datetime.date(2032, 11, 15),
        datetime.date(2033, 2, 28),
        datetime.date(2033, 3, 1),
        datetime.date(2033, 4, 15),
        datetime.date(2033, 4, 21),
        datetime.date(2033, 6, 16),
        datetime.date(2033, 9, 7),
        datetime.date(2033, 10, 12),
        datetime.date(2033, 11, 2),
        datetime.date(2033, 11, 15),
        datetime.date(2034, 2, 20),
        datetime.date(2034, 2, 21),
        datetime.date(2034, 4, 7),
        datetime.date(2034, 4, 21),
        datetime.date(2034, 5, 1),
        datetime.date(2034, 6, 8),
        datetime.date(2034, 9, 7),
        datetime.date(2034, 10, 12),
        datetime.date(2034, 11, 2),
        datetime.date(2034, 11, 15),
        datetime.date(2034, 12, 25),
        datetime.date(2035, 1, 1),
        datetime.date(2035, 2, 5),
        datetime.date(2035, 2, 6),
        datetime.date(2035, 3, 23),
        datetime.date(2035, 5, 1),
        datetime.date(2035, 5, 24),
        datetime.date(2035, 9, 7),
        datetime.date(2035, 10, 12),
        datetime.date(2035, 11, 2),
        datetime.date(2035, 11, 15),
        datetime.date(2035, 12, 25),
        datetime.date(2036, 1, 1),
        datetime.date(2036, 2, 25),
        datetime.date(2036, 2, 26),
        datetime.date(2036, 4, 11),
        datetime.date(2036, 4, 21),
        datetime.date(2036, 5, 1),
        datetime.date(2036, 6, 12),
        datetime.date(2036, 12, 25),
        datetime.date(2037, 1, 1),
        datetime.date(2037, 2, 16),
        datetime.date(2037, 2, 17),
        datetime.date(2037, 4, 3),
        datetime.date(2037, 4, 21),
        datetime.date(2037, 5, 1),
        datetime.date(2037, 6, 4),
        datetime.date(2037, 9, 7),
        datetime.date(2037, 10, 12),
        datetime.date(2037, 11, 2),
        datetime.date(2037, 12, 25),
        datetime.date(2038, 1, 1),
        datetime.date(2038, 3, 8),
        datetime.date(2038, 3, 9),
        datetime.date(2038, 4, 21),
        datetime.date(2038, 4, 23),
        datetime.date(2038, 6, 24),
        datetime.date(2038, 9, 7),
        datetime.date(2038, 10, 12),
        datetime.date(2038, 11, 2),
        datetime.date(2038, 11, 15),
        datetime.date(2039, 2, 21),
        datetime.date(2039, 2, 22),
        datetime.date(2039, 4, 8),
        datetime.date(2039, 4, 21),
        datetime.date(2039, 6, 9),
        datetime.date(2039, 9, 7),
        datetime.date(2039, 10, 12),
        datetime.date(2039, 11, 2),
        datetime.date(2039, 11, 15),
        datetime.date(2040, 2, 13),
        datetime.date(2040, 2, 14),
        datetime.date(2040, 3, 30),
        datetime.date(2040, 5, 1),
        datetime.date(2040, 5, 31),
        datetime.date(2040, 9, 7),
        datetime.date(2040, 10, 12),
        datetime.date(2040, 11, 2),
        datetime.date(2040, 11, 15),
        datetime.date(2040, 12, 25),
        datetime.date(2041, 1, 1),
        datetime.date(2041, 3, 4),
        datetime.date(2041, 3, 5),
        datetime.date(2041, 4, 19),
        datetime.date(2041, 5, 1),
        datetime.date(2041, 6, 20),
        datetime.date(2041, 11, 15),
        datetime.date(2041, 12, 25),
        datetime.date(2042, 1, 1),
        datetime.date(2042, 2, 17),
        datetime.date(2042, 2, 18),
        datetime.date(2042, 4, 4),
        datetime.date(2042, 4, 21),
        datetime.date(2042, 5, 1),
        datetime.date(2042, 6, 5),
        datetime.date(2042, 12, 25),
        datetime.date(2043, 1, 1),
        datetime.date(2043, 2, 9),
        datetime.date(2043, 2, 10),
        datetime.date(2043, 3, 27),
        datetime.date(2043, 4, 21),
        datetime.date(2043, 5, 1),
        datetime.date(2043, 5, 28),
        datetime.date(2043, 9, 7),
        datetime.date(2043, 10, 12),
        datetime.date(2043, 11, 2),
        datetime.date(2043, 12, 25),
        datetime.date(2044, 1, 1),
        datetime.date(2044, 2, 29),
        datetime.date(2044, 3, 1),
        datetime.date(2044, 4, 15),
        datetime.date(2044, 4, 21),
        datetime.date(2044, 6, 16),
        datetime.date(2044, 9, 7),
        datetime.date(2044, 10, 12),
        datetime.date(2044, 11, 2),
        datetime.date(2044, 11, 15),
        datetime.date(2045, 2, 20),
        datetime.date(2045, 2, 21),
        datetime.date(2045, 4, 7),
        datetime.date(2045, 4, 21),
        datetime.date(2045, 5, 1),
        datetime.date(2045, 6, 8),
        datetime.date(2045, 9, 7),
        datetime.date(2045, 10, 12),
        datetime.date(2045, 11, 2),
        datetime.date(2045, 11, 15),
        datetime.date(2045, 12, 25),
        datetime.date(2046, 1, 1),
        datetime.date(2046, 2, 5),
        datetime.date(2046, 2, 6),
        datetime.date(2046, 3, 23),
        datetime.date(2046, 5, 1),
        datetime.date(2046, 5, 24),
        datetime.date(2046, 9, 7),
        datetime.date(2046, 10, 12),
        datetime.date(2046, 11, 2),
        datetime.date(2046, 11, 15),
        datetime.date(2046, 12, 25),
        datetime.date(2047, 1, 1),
        datetime.date(2047, 2, 25),
        datetime.date(2047, 2, 26),
        datetime.date(2047, 4, 12),
        datetime.date(2047, 5, 1),
        datetime.date(2047, 6, 13),
        datetime.date(2047, 11, 15),
        datetime.date(2047, 12, 25),
        datetime.date(2048, 1, 1),
        datetime.date(2048, 2, 17),
        datetime.date(2048, 2, 18),
        datetime.date(2048, 4, 3),
        datetime.date(2048, 4, 21),
        datetime.date(2048, 5, 1),
        datetime.date(2048, 6, 4),
        datetime.date(2048, 9, 7),
        datetime.date(2048, 10, 12),
        datetime.date(2048, 11, 2),
        datetime.date(2048, 12, 25),
        datetime.date(2049, 1, 1),
        datetime.date(2049, 3, 1),
        datetime.date(2049, 3, 2),
        datetime.date(2049, 4, 16),
        datetime.date(2049, 4, 21),
        datetime.date(2049, 6, 17),
        datetime.date(2049, 9, 7),
        datetime.date(2049, 10, 12),
        datetime.date(2049, 11, 2),
        datetime.date(2049, 11, 15),
        datetime.date(2050, 2, 21),
        datetime.date(2050, 2, 22),
        datetime.date(2050, 4, 8),
        datetime.date(2050, 4, 21),
        datetime.date(2050, 6, 9),
        datetime.date(2050, 9, 7),
        datetime.date(2050, 10, 12),
        datetime.date(2050, 11, 2),
        datetime.date(2050, 11, 15),
        datetime.date(2051, 2, 13),
        datetime.date(2051, 2, 14),
        datetime.date(2051, 3, 31),
        datetime.date(2051, 4, 21),
        datetime.date(2051, 5, 1),
        datetime.date(2051, 6, 1),
        datetime.date(2051, 9, 7),
        datetime.date(2051, 10, 12),
        datetime.date(2051, 11, 2),
        datetime.date(2051, 11, 15),
        datetime.date(2051, 12, 25),
        datetime.date(2052, 1, 1),
        datetime.date(2052, 3, 4),
        datetime.date(2052, 3, 5),
        datetime.date(2052, 4, 19),
        datetime.date(2052, 5, 1),
        datetime.date(2052, 6, 20),
        datetime.date(2052, 11, 15),
        datetime.date(2052, 12, 25),
        datetime.date(2053, 1, 1),
        datetime.date(2053, 2, 17),
        datetime.date(2053, 2, 18),
        datetime.date(2053, 4, 4),
        datetime.date(2053, 4, 21),
        datetime.date(2053, 5, 1),
        datetime.date(2053, 6, 5),
        datetime.date(2053, 12, 25),
        datetime.date(2054, 1, 1),
        datetime.date(2054, 2, 9),
        datetime.date(2054, 2, 10),
        datetime.date(2054, 3, 27),
        datetime.date(2054, 4, 21),
        datetime.date(2054, 5, 1),
        datetime.date(2054, 5, 28),
        datetime.date(2054, 9, 7),
        datetime.date(2054, 10, 12),
        datetime.date(2054, 11, 2),
        datetime.date(2054, 12, 25),
        datetime.date(2055, 1, 1),
        datetime.date(2055, 3, 1),
        datetime.date(2055, 3, 2),
        datetime.date(2055, 4, 16),
        datetime.date(2055, 4, 21),
        datetime.date(2055, 6, 17),
        datetime.date(2055, 9, 7),
        datetime.date(2055, 10, 12),
        datetime.date(2055, 11, 2),
        datetime.date(2055, 11, 15),
        datetime.date(2056, 2, 14),
        datetime.date(2056, 2, 15),
        datetime.date(2056, 3, 31),
        datetime.date(2056, 4, 21),
        datetime.date(2056, 5, 1),
        datetime.date(2056, 6, 1),
        datetime.date(2056, 9, 7),
        datetime.date(2056, 10, 12),
        datetime.date(2056, 11, 2),
        datetime.date(2056, 11, 15),
        datetime.date(2056, 12, 25),
        datetime.date(2057, 1, 1),
        datetime.date(2057, 3, 5),
        datetime.date(2057, 3, 6),
        datetime.date(2057, 4, 20),
        datetime.date(2057, 5, 1),
        datetime.date(2057, 6, 21),
        datetime.date(2057, 9, 7),
        datetime.date(2057, 10, 12),
        datetime.date(2057, 11, 2),
        datetime.date(2057, 11, 15),
        datetime.date(2057, 12, 25),
        datetime.date(2058, 1, 1),
        datetime.date(2058, 2, 25),
        datetime.date(2058, 2, 26),
        datetime.date(2058, 4, 12),
        datetime.date(2058, 5, 1),
        datetime.date(2058, 6, 13),
        datetime.date(2058, 11, 15),
        datetime.date(2058, 12, 25),
        datetime.date(2059, 1, 1),
        datetime.date(2059, 2, 10),
        datetime.date(2059, 2, 11),
        datetime.date(2059, 3, 28),
        datetime.date(2059, 4, 21),
        datetime.date(2059, 5, 1),
        datetime.date(2059, 5, 29),
        datetime.date(2059, 12, 25),
        datetime.date(2060, 1, 1),
        datetime.date(2060, 3, 1),
        datetime.date(2060, 3, 2),
        datetime.date(2060, 4, 16),
        datetime.date(2060, 4, 21),
        datetime.date(2060, 6, 17),
        datetime.date(2060, 9, 7),
        datetime.date(2060, 10, 12),
        datetime.date(2060, 11, 2),
        datetime.date(2060, 11, 15),
        datetime.date(2061, 2, 21),
        datetime.date(2061, 2, 22),
        datetime.date(2061, 4, 8),
        datetime.date(2061, 4, 21),
        datetime.date(2061, 6, 9),
        datetime.date(2061, 9, 7),
        datetime.date(2061, 10, 12),
        datetime.date(2061, 11, 2),
        datetime.date(2061, 11, 15),
        datetime.date(2062, 2, 6),
        datetime.date(2062, 2, 7),
        datetime.date(2062, 3, 24),
        datetime.date(2062, 4, 21),
        datetime.date(2062, 5, 1),
        datetime.date(2062, 5, 25),
        datetime.date(2062, 9, 7),
        datetime.date(2062, 10, 12),
        datetime.date(2062, 11, 2),
        datetime.date(2062, 11, 15),
        datetime.date(2062, 12, 25),
        datetime.date(2063, 1, 1),
        datetime.date(2063, 2, 26),
        datetime.date(2063, 2, 27),
        datetime.date(2063, 4, 13),
        datetime.date(2063, 5, 1),
        datetime.date(2063, 6, 14),
        datetime.date(2063, 9, 7),
        datetime.date(2063, 10, 12),
        datetime.date(2063, 11, 2),
        datetime.date(2063, 11, 15),
        datetime.date(2063, 12, 25),
        datetime.date(2064, 1, 1),
        datetime.date(2064, 2, 18),
        datetime.date(2064, 2, 19),
        datetime.date(2064, 4, 4),
        datetime.date(2064, 4, 21),
        datetime.date(2064, 5, 1),
        datetime.date(2064, 6, 5),
        datetime.date(2064, 12, 25),
        datetime.date(2065, 1, 1),
        datetime.date(2065, 2, 9),
        datetime.date(2065, 2, 10),
        datetime.date(2065, 3, 27),
        datetime.date(2065, 4, 21),
        datetime.date(2065, 5, 1),
        datetime.date(2065, 5, 28),
        datetime.date(2065, 9, 7),
        datetime.date(2065, 10, 12),
        datetime.date(2065, 11, 2),
        datetime.date(2065, 12, 25),
        datetime.date(2066, 1, 1),
        datetime.date(2066, 2, 22),
        datetime.date(2066, 2, 23),
        datetime.date(2066, 4, 9),
        datetime.date(2066, 4, 21),
        datetime.date(2066, 6, 10),
        datetime.date(2066, 9, 7),
        datetime.date(2066, 10, 12),
        datetime.date(2066, 11, 2),
        datetime.date(2066, 11, 15),
        datetime.date(2067, 2, 14),
        datetime.date(2067, 2, 15),
        datetime.date(2067, 4, 1),
        datetime.date(2067, 4, 21),
        datetime.date(2067, 6, 2),
        datetime.date(2067, 9, 7),
        datetime.date(2067, 10, 12),
        datetime.date(2067, 11, 2),
        datetime.date(2067, 11, 15),
        datetime.date(2068, 3, 5),
        datetime.date(2068, 3, 6),
        datetime.date(2068, 4, 20),
        datetime.date(2068, 5, 1),
        datetime.date(2068, 6, 21),
        datetime.date(2068, 9, 7),
        datetime.date(2068, 10, 12),
        datetime.date(2068, 11, 2),
        datetime.date(2068, 11, 15),
        datetime.date(2068, 12, 25),
        datetime.date(2069, 1, 1),
        datetime.date(2069, 2, 25),
        datetime.date(2069, 2, 26),
        datetime.date(2069, 4, 12),
        datetime.date(2069, 5, 1),
        datetime.date(2069, 6, 13),
        datetime.date(2069, 11, 15),
        datetime.date(2069, 12, 25),
        datetime.date(2070, 1, 1),
        datetime.date(2070, 2, 10),
        datetime.date(2070, 2, 11),
        datetime.date(2070, 3, 28),
        datetime.date(2070, 4, 21),
        datetime.date(2070, 5, 1),
        datetime.date(2070, 5, 29),
        datetime.date(2070, 12, 25),
        datetime.date(2071, 1, 1),
        datetime.date(2071, 3, 2),
        datetime.date(2071, 3, 3),
        datetime.date(2071, 4, 17),
        datetime.date(2071, 4, 21),
        datetime.date(2071, 5, 1),
        datetime.date(2071, 6, 18),
        datetime.date(2071, 9, 7),
        datetime.date(2071, 10, 12),
        datetime.date(2071, 11, 2),
        datetime.date(2071, 12, 25),
        datetime.date(2072, 1, 1),
        datetime.date(2072, 2, 22),
        datetime.date(2072, 2, 23),
        datetime.date(2072, 4, 8),
        datetime.date(2072, 4, 21),
        datetime.date(2072, 6, 9),
        datetime.date(2072, 9, 7),
        datetime.date(2072, 10, 12),
        datetime.date(2072, 11, 2),
        datetime.date(2072, 11, 15),
        datetime.date(2073, 2, 6),
        datetime.date(2073, 2, 7),
        datetime.date(2073, 3, 24),
        datetime.date(2073, 4, 21),
        datetime.date(2073, 5, 1),
        datetime.date(2073, 5, 25),
        datetime.date(2073, 9, 7),
        datetime.date(2073, 10, 12),
        datetime.date(2073, 11, 2),
        datetime.date(2073, 11, 15),
        datetime.date(2073, 12, 25),
        datetime.date(2074, 1, 1),
        datetime.date(2074, 2, 26),
        datetime.date(2074, 2, 27),
        datetime.date(2074, 4, 13),
        datetime.date(2074, 5, 1),
        datetime.date(2074, 6, 14),
        datetime.date(2074, 9, 7),
        datetime.date(2074, 10, 12),
        datetime.date(2074, 11, 2),
        datetime.date(2074, 11, 15),
        datetime.date(2074, 12, 25),
        datetime.date(2075, 1, 1),
        datetime.date(2075, 2, 18),
        datetime.date(2075, 2, 19),
        datetime.date(2075, 4, 5),
        datetime.date(2075, 5, 1),
        datetime.date(2075, 6, 6),
        datetime.date(2075, 11, 15),
        datetime.date(2075, 12, 25),
        datetime.date(2076, 1, 1),
        datetime.date(2076, 3, 2),
        datetime.date(2076, 3, 3),
        datetime.date(2076, 4, 17),
        datetime.date(2076, 4, 21),
        datetime.date(2076, 5, 1),
        datetime.date(2076, 6, 18),
        datetime.date(2076, 9, 7),
        datetime.date(2076, 10, 12),
        datetime.date(2076, 11, 2),
        datetime.date(2076, 12, 25),
        datetime.date(2077, 1, 1),
        datetime.date(2077, 2, 22),
        datetime.date(2077, 2, 23),
        datetime.date(2077, 4, 9),
        datetime.date(2077, 4, 21),
        datetime.date(2077, 6, 10),
        datetime.date(2077, 9, 7),
        datetime.date(2077, 10, 12),
        datetime.date(2077, 11, 2),
        datetime.date(2077, 11, 15),
        datetime.date(2078, 2, 14),
        datetime.date(2078, 2, 15),
        datetime.date(2078, 4, 1),
        datetime.date(2078, 4, 21),
        datetime.date(2078, 6, 2),
        datetime.date(2078, 9, 7),
        datetime.date(2078, 10, 12),
        datetime.date(2078, 11, 2),
        datetime.date(2078, 11, 15)
    )
    return feriados