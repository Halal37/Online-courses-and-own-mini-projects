*&---------------------------------------------------------------------*
*& Report Y_JZA_10
*&---------------------------------------------------------------------*
*&Autor" Wojciech Lidwin
*&---------------------------------------------------------------------*
REPORT Y_JZA_10.

data lv_text type string.

lv_text = 'Wojciech Lidwin Moj pierwszy program'.

"set 'Text' to lv_text.
*set 'Text' to lv_text.

data: lv_imie type char20,
      lv_nazwisko type char40.

data lv_wiek type i value 20. "liczba ca³kowita"
data lv_num type f.
lv_num = 10 / '1.5' .

split lv_text at ' ' into lv_imie lv_nazwisko data(lv_reszta).

write: lv_imie, lv_nazwisko, lv_num.

split lv_text at ' ' into table data(it_slowa).

lv_num = LINES( it_slowa ).

write: | { 'Liczba wierszy' }={ LINES( it_slowa ) }|.

loop at it_slowa into data(lv_slowo).
 write: / SY-TABIX, lv_slowo.

endloop.

loop at it_slowa into lv_slowo.
  if lv_slowo CP 'p*'.
    write: / SY-TABIX, lv_slowo.
    endif.
 endloop.
data lv_znaleziony type abap_bool.
Write: /' '.

if LV_ZNALEZIONY EQ 'X'.
  write: / 'Znalezione', Sy-tabix.
endif.