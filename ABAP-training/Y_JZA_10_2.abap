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
data lv_str type string.
data it_slowa type STANDARD TABLE OF ts_opis_slowa.
data is_palindrom type abap_bool.

parameters: p_dlug type i DEFAULT 4.
parameters: p_pat type char10 DEFAULT '*ad*'.

START-OF-SELECTION.
*data it_slowa type STANDARD TABLE OF ts_opis_slowa.
it_slowa = VALUE #(
( slowo ='kajak' )
).
select slowo from YJZA_PALINDROM10 into CORRESPONDING FIELDS OF table it_slowa.

write: | { 'Liczba wierszy' }={ LINES( it_slowa ) }|.

loop at it_slowa into data(lv_slowo) where SLOWO CP p_pat.
* if SY-TABIX LE 10.
* write: / SY-TABIX, lv_slowo-SLOWO.
* perform odwroc_slowo using lv_slowo-SLOWO changing lv_str.
* write: /'Slowo ', lv_slowo-SLOWO, ' Odwrocone slowo ', lv_str.
 if strlen( lv_slowo-SLOWO ) = p_dlug or p_dlug LE 0.
 PERFORM CZY_PALINDROM
 USING lv_slowo-SLOWO
 CHANGING is_palindrom.
 if is_palindrom EQ abap_true.
 write: / SY-TABIX,lv_slowo-SLOWO, 'Palindrom? ',is_palindrom.
 endif.
 endif.
endloop.

*loop at it_slowa into lv_slowo.
*  if lv_slowo-SLOWO CP 'W*'.
*    write: / SY-TABIX, lv_slowo-SLOWO.
*    else.
*    endif.
*    endloop.

form czy_palindrom using p_slowo type string
      changing out_palindrom type abap_bool.

data lv_slowo_odr type string.

perform odwroc_slowo using p_slowo changing lv_slowo_odr.
if lv_slowo_odr EQ p_slowo.
  out_palindrom = 'X'.
  else.
    out_palindrom = abap_false.
    endif.
endform.

form odwroc_slowo using p_slowo type string changing out_slowo_odr type string.

data lv_dlugosc type i.
data lv_znak type char01.
data lv_pos type i.

lv_dlugosc = strlen( p_slowo ).
lv_pos = lv_dlugosc - 1.

while lv_pos >= 0.
  lv_znak = p_slowo+lv_pos(1).
*  write: /'znak ', lv_znak,lv_pos.
  concatenate out_slowo_odr lv_znak into out_slowo_odr.
  subtract 1 from lv_pos.
  endwhile.

endform.