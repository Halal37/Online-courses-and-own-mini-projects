FUNCTION Y_JZA_SLOWA_HASH_TAB10.
*"----------------------------------------------------------------------
*"*"Local Interface:
*"----------------------------------------------------------------------

DATA gt_dict_word type hashed TABLE OF yjza_english with unique key word.
select * from yjza_english into CORRESPONDING FIELDS OF TABLE gt_dict_word.
  data p_num type int4 value 10000.
  do p_num times.
    read table gt_dict_word with table key word = 'zoo' TRANSPORTING no FIELDS.
    cl_demo_output=>display( gt_dict_word ).
    enddo.

    do p_num times.
      read table gt_dict_word with table key word = 'xxxxxxx' TRANSPORTING no FIELDS.
      cl_demo_output=>display( gt_dict_word ).
      enddo.



ENDFUNCTION.