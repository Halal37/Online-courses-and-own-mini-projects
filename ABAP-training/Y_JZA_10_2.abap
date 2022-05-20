*&---------------------------------------------------------------------*
*& Report Y_JZA_10
*&---------------------------------------------------------------------*
*&Autor" Wojciech Lidwin
*&---------------------------------------------------------------------*
REPORT Y_JZA_10_2.

TYPES: begin of ts_opis_slowa,
  mandt type mandt,
  slowo type string,
  end of ts_opis_slowa.

data lv_text type string.

data it_slowa type STANDARD TABLE OF ts_opis_slowa.


write: | { 'Liczba wierszy' }={ LINES( it_slowa ) }|.

loop at it_slowa into data(lv_slowo).
 if SY-TABIX LE 10.
 write: / SY-TABIX, lv_slowo-SLOWO.
 else.
   exit.
 endif.
endloop.

loop at it_slowa into lv_slowo.
  if lv_slowo-SLOWO CP 'W*'.
    write: / SY-TABIX, lv_slowo-SLOWO.
    else.
    endif.
    endloop.