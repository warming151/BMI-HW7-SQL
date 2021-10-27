with pID as
(
SELECT st.icustay_id, st.charttime, st.creat, st.aki_stage_creat,
st.aki_stage_uo, st.aki_stage, it.SUBJECT_ID, it.HADM_ID
FROM `physionet-data.mimiciii_derived.kdigo_stages` st
LEFT JOIN `physionet-data.mimiciii_clinical.icustays` it
ON st.icustay_id =it.ICUSTAY_ID
)
SELECT DISTINCT pID.SUBJECT_ID, pID.icustay_id, pID.aki_stage, bg.SPECIMEN_PROB, l1.PotassiumVALUENUM, l2.SodiumVALUENUM,
l3.ChlorideVALUENUM, l4.GlucoseVALUENUM, l5.BloodCulturesVALUENUM, l6.RedBloodCVALUENUM, l7.BaselinepainlevelVALUENUM,
ap.hematocrit_score, ap.creatinine_score
FROM pID 
LEFT JOIN `physionet-data.mimiciii_derived.bloodgasfirstdayarterial` bg 
on pID.icustay_id = bg.icustay_id
LEFT JOIN `innate-algebra-328912.hmhm.LABEL1` l1
on pID.icustay_id = l1.icustay_id
LEFT JOIN `innate-algebra-328912.hmhm.LABEL2` l2
on pID.icustay_id = l2.icustay_id
LEFT JOIN `innate-algebra-328912.hmhm.LABEL3` l3
on pID.icustay_id = l3.icustay_id
LEFT JOIN `innate-algebra-328912.hmhm.LABEL4` l4
on pID.icustay_id = l4.icustay_id
LEFT JOIN `innate-algebra-328912.hmhm.LABEL5` l5
on pID.icustay_id = l5.icustay_id
LEFT JOIN `innate-algebra-328912.hmhm.LABEL6` l6
on pID.icustay_id = l6.icustay_id
LEFT JOIN `innate-algebra-328912.hmhm.LABEL7` l7
on pID.icustay_id = l7.icustay_id
LEFT JOIN `physionet-data.mimiciii_derived.apsiii` ap
on pID.icustay_id = ap.icustay_id


