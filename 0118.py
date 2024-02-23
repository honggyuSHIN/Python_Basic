#########################################
# ※ KOI 제품은 6개의 숫자 조합으로 이루어져 있으며, 제품코드 판별 5자리와 검증코드 1자리 조합으로 배치된다.
# 제품코드 5자리 각각을 제곱하여 합해준 값의 1의 자리가 마지막 6번째 수와 일치할 경우 KOI 제품이라고 한다.
# ======================================
# 325321  > 9 + 4 + 25 + 9 + 4 > 51   
# 51 의 일의자리와 마지막 1이 같으므로 KOI 제품
# ======================================

st='''
941301
952438
799400
586338
821562
138018
835828
436240
441605
606177
971321
364976
155552
654670
753942
265414
296562
991907
707509
459687
154857
179920
604417
409457
856451
746464
260366
207258
984908
242966
753251
427944
275221
868254
825521
315435
254136
387735
611032
984826
899359
816999
406456
797273
878171
352530
164003
391721
833889
162380
421587
371664
909106
839077
757790
352674
493486
906703
378168
362316
340685
669231
492876
944857
640339
181904
506265
322961
214687
537958
832104
768977
103032
388416
870541
547753
487287
695298
528946
672092
133398
684637
837241
549334
153169
504033
619439
441957
535227
259628
739497
864744
409822
707021
153447
139894
300589
225006
577145
220012
915867
548899
785861
130601
182503
556549
192733
863275
831200
666599
202360
451630
674178
178400
518845
155236
297389
248017
688934
408055
840907
514332
816056
878237
966564
291149
320932
238468
134174
559398
695021
754360
797872
600639
381582
181900
716190
230362
986320
293402
569062
666115
202037
851254
632286
866152
643229
734085
790512
199990
468230
582676
654153
142335
453164
787115
714263
166956
220604
541908
359656
104420
412299
585969
858155
955311
653127
330881
880605
111607
419438
111395
970483
829643
903396
377267
968691
578465
373660
369529
812810
573410
124117
421199
855459
633365
771307
343594
854308
584454
567906
995146
680327
244440
165748
845857
804841
156225
129413
134667
323371
531450
880245
230745
684298
615298
962052
654847
605545
412141
737026
885699
509128
520156
822366
625780
651566
153788
116224
501712
608021
332353
371783
518120
667525
959112
203450
371415
519487
115481
392845
589063
131700
123914
484383
155695
998293
863250
937343
633605
871039
357769
357972
679540
286559
237989
962966
362237
393832
494793
963622
542727
359821
641483
794921
367071
908262
784720
510621
641803
478579
816780
479591
254370
873609
417657
182743
732909
628345
967515
513577
429113
272188
667299
322924
169807
867661
300672
172042
391761
415044
848244
451884
546924
610243
269913
850339
768853
121758
257378
667028
249508
464854
981358
897152
947404
262629
422162
967382
474980
770183
452812
565421
882091
806539
705035
190043
364884
487111
249552
571934
774492
437163
489632
774882
898783
407249
806393
818214
551106
307685
753298
777246
485657
542757
935632
536854
113617
920117
782079
677185
787552
421434
322993
698261
596554
188587
322646
350165
169054
533123
978960
708626
652673
540385
378526
794448
766475
550257
656462
685111
992773
348128
655749
948443
706654
170890
159294
755795
194731
503693
345887
949696
707403
695786
387252
539833
165903
784180
423082
244291
685908
857294
545855
717226
912202
697051
500857
802570
879364
574751
180105
484838
233016
608316
472606
552808
663279
426178
563743
129502
846371
194073
806526
856390
749470
177913
159923
363342
426539
407257
793572
151829
590797
865634
988828
107324
219559
407930
858412
932970
985350
255845
232313
305486
986846
919195
947448
474120
323076
861251
171547
998402
199984
456215
405840
903162
513515
507127
756083
429409
794591
719748
631869
220610
970527
600908
176916
678095
803228
910065
753274
349601
314061
177060
978211
825811
145469
459197
541910
525104
794821
339159
780357
454955
696399
856528
511494
405878
297589
965269
215998
180593
930396
558815
220549
840809
907307
608705
777460
452825
612784
127019
203604
314456
304575
254182
314679
728983
198546
193125
678299
467673
873016
744745
407723
679677
192776
403281
956865
129935
393924
447761
236308
604920
468642
473779
432037
434187
574909
676370
863321
132767
814681
272205
795469
225629
519115
330655
178163
907053
243608
398209
912961
575401
609206
428887
811380
883589
776347
743808
570517
523675
915924
197081
230356
939797
363055
410694
292271
298851
854237
879516
129275
834396
333110
984537
833736
547625
341013
915769
589537
325822
413548
191445
451247
895167
939684
595281
784537
429588
377742
301210
176614
865504
204355
526624
736795
825138
567862
110574
125248
853967
614590
997358
172970
643481
185047
588245
505347
289365
834753
153781
380435
167445
316682
855083
886963
454223
586497
350821
800074
761479
356354
930060
978542
323782
856784
957029
893382
894770
369544
374877
382890
148617
581682
935027
110812
424085
935269
281287
713295
723559
684725
841827
277628
667782
198023
495436
156627
912892
538885
319968
232513
149940
651729
481386
914069
558732
309557
107300
802403
507844
713439
734297
984492
267393
666926
428361
565228
906065
664727
598195
485320
657954
494386
358230
343331
252830
319069
189455
476588
438050
938092
235679
741267
211716
564909
193143
257122
188589
467678
347191
248111
420299
187466
493989
886002
729651
290792
218378
788940
665408
250585
202240
795738
982601
493022
178849
313971
367751
303123
618826
758169
145567
768512
763752
362088
227015
814165
752918
188970
496724
401295
740556
606537
276135
127201
315329
313069
795073
678252
512030
853496
524894
493953
122846
153628
686034
211942
546373
628434
321643
470913
229273
193942
472803
862239
158574
705045
966269
317222
703754
384394
103430
903501
919174
245838
990718
274565
315045
174837
564151
227141
773679
213159
350200
569185
586230
651882
993305
955507
431979
415969
114491
709942
658955
492602
578629
372094
661996
351805
463364
279466
693491
592194
575233
696844
728335
671631
506509
222018
459129
742994
919302
237575
465939
668407
508214
151041
925769
723004
645528
519912
936522
141376
808627
762803
602598
614693
219699
398149
280530
796681
713327
219082
370124
782930
424741
171658
669091
650861
291264
603026
980227
844630
978104
721326
215806
206267
778232
652910
378413
405177
186629
348942
517734
851831
654271
975856
495273
265426
449423
999782
158129
283169
762789
474830
710935
276976
675458
581708
938385
122068
822795
780620
679834
360821
792687
359567
847990
143112
480775
469392
524267
386497
922817
993473
554195
786887
205182
769819
922705
536285
373282
449537
230059
876694
852993
716061
635866
811152
161769
808528
286703
781277
276182
206852
574650
436338
408677
325820
739350
640295
548552
404637
244553
776592
773679
770879
338730
627704
480685
153316
649210
378232
895794
115590
718436
325708
406262
646796
692019
548253
535503
394414
512379
270732
868466
419621
743394
707628
129528
448135
927045
515393
786188
875211
272085
188406
153112
558133
625663
251190
163141
784275
809911
371050
173366
902250
783838
510007
816564
769285
142177
469054
333840
394367
472621
465841
179515
142772
523709
881541
827685
612743
197994
469256
262823
674718
731932
929895
486329
187977
217567
184426
861222
413777
284505
926618
820102
458027
690398
919550
425625
681930
190321
861419
553011
309581
540030
124490
196737
294046
564196
628474
125866
774965
400448
603084
686016
272048
248646
349560
878815
274245
557388
603645
319663
542696
173267
585252
906698
253943
335557
710056
857583
515604
267417
176162
346604
285575
804861
966467
644482
248427
641571
903485
260186
956592
153561
131986
150698
249679
483380
282636
726566
511039
551691
151511
499705
726538
739849
444233
974116
536407
822029
304771
581860
684014

'''
su=0

li=st.split()                  #리스트로 바꿈.

for i in li:                    #리스트에 들어있는 문자열을 하나씩 대입.
    hap=0
    for j in i:                 #문자열의 문자를 하나씩 대입.
        hap+=int(j)**2 
             #정수로 바꿔서 제곱 후 더함.
    hap-=int(j)**2              #반복문에서 빠져나와서 마지막 j의 값을 다시 뺌.
    
    if hap<20:
        print(hap,i,j)      

    ###j값 뭔지 계산해보기.           
    
    if hap%10==int(j):
        su+=1
print(su)
