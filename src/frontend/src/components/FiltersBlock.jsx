import ToggleFalseStateDefaultL from "./ToggleFalseStateDefaultL";
import HabrRating from "./HabrRating";
import FilledNoStateDefaultSize from "./FilledNoStateDefaultSize";
import StyleOutlineTypetextClea from "./StyleOutlineTypetextClea";
import styles from "./FiltersBlock.module.css";

const FiltersBlock = () => {
  return (
    <div className={styles.filtersBlock}>
      <div className={styles.userPlatform}>
        <b className={styles.b}>Откуда пользователь?</b>
        <div className={styles.platformList}>
          <ToggleFalseStateDefaultL
            group1="/group-1.svg"
            radioButton="С ХабраЛинкера"
            toggleFalseStateDefaultLPosition="unset"
            toggleFalseStateDefaultLTop="unset"
            toggleFalseStateDefaultLLeft="unset"
            radioButtonFontFamily="Inika"
          />
          <ToggleFalseStateDefaultL
            group1="/group-1.svg"
            radioButton="С Хабра"
            toggleFalseStateDefaultLPosition="unset"
            toggleFalseStateDefaultLTop="unset"
            toggleFalseStateDefaultLLeft="unset"
            radioButtonFontFamily="Inika"
          />
          <ToggleFalseStateDefaultL
            group1="/group-3.svg"
            radioButton="С любой платформы"
            toggleFalseStateDefaultLPosition="unset"
            toggleFalseStateDefaultLTop="unset"
            toggleFalseStateDefaultLLeft="unset"
            radioButtonFontFamily="Poppins"
          />
        </div>
      </div>
      <HabrRating
        prop="Рейтинг хабра"
        label="4.5"
        label1="5"
        showIcon={false}
      />
      <HabrRating
        prop="Карма хабра"
        label="100"
        label1="-"
        propOverflow="hidden"
        propWidth="unset"
        showIcon={false}
      />
      <div className={styles.userPlatform}>
        <b className={styles.b}>Пол</b>
        <div className={styles.genderList}>
          <ToggleFalseStateDefaultL
            group1="/group-1.svg"
            radioButton="Любой"
            toggleFalseStateDefaultLPosition="absolute"
            toggleFalseStateDefaultLTop="0px"
            toggleFalseStateDefaultLLeft="0px"
            radioButtonFontFamily="Inika"
          />
          <ToggleFalseStateDefaultL
            group1="/group-3.svg"
            radioButton="Мужской"
            toggleFalseStateDefaultLPosition="absolute"
            toggleFalseStateDefaultLTop="26px"
            toggleFalseStateDefaultLLeft="0px"
            radioButtonFontFamily="Inika"
          />
          <ToggleFalseStateDefaultL
            group1="/group-1.svg"
            radioButton="Женский"
            toggleFalseStateDefaultLPosition="absolute"
            toggleFalseStateDefaultLTop="52px"
            toggleFalseStateDefaultLLeft="0px"
            radioButtonFontFamily="Poppins"
          />
        </div>
      </div>
      <HabrRating
        prop="Возраст"
        label="0"
        label1="99"
        propOverflow="unset"
        propWidth="78px"
        showIcon={false}
      />
      <div className={styles.place}>
        <b className={styles.b}>Место</b>
        <div className={styles.placeFields}>
          <FilledNoStateDefaultSize
            tangoUser="/tangolock1.svg"
            label="Англия"
            showIcon={false}
            filledNoStateDefaultSizeWidth="unset"
            filledNoStateDefaultSizeHeight="27px"
            filledNoStateDefaultSizePadding="0px var(--padding-base)"
            filledNoStateDefaultSizeOverflow="unset"
            filledNoStateDefaultSizeAlignSelf="stretch"
            labelFontFamily="'Inria Sans'"
          />
          <FilledNoStateDefaultSize
            tangoUser="/tangolock1.svg"
            label="Бирмингем"
            showIcon={false}
            filledNoStateDefaultSizeWidth="unset"
            filledNoStateDefaultSizeHeight="27px"
            filledNoStateDefaultSizePadding="0px var(--padding-base)"
            filledNoStateDefaultSizeOverflow="unset"
            filledNoStateDefaultSizeAlignSelf="stretch"
            labelFontFamily="'Inria Sans'"
          />
          <FilledNoStateDefaultSize
            tangoUser="/tangolock1.svg"
            label="Смоллхит"
            showIcon={false}
            filledNoStateDefaultSizeWidth="unset"
            filledNoStateDefaultSizeHeight="27px"
            filledNoStateDefaultSizePadding="0px var(--padding-base)"
            filledNoStateDefaultSizeOverflow="unset"
            filledNoStateDefaultSizeAlignSelf="stretch"
            labelFontFamily="'Inria Sans'"
          />
        </div>
      </div>
      <HabrRating
        prop="Зарплата"
        label="0"
        label1="1000000"
        propOverflow="hidden"
        propWidth="unset"
        showIcon={false}
      />
      <div className={styles.place}>
        <b className={styles.b}>Специальности</b>
        <div className={styles.specialitiesField}>
          <StyleOutlineTypetextClea
            label="Рэкетирство "
            styleOutlineTypetextCleaBorder="1px solid var(--color-steelblue-100)"
          />
        </div>
      </div>
      <div className={styles.place}>
        <b className={styles.b}>Умения</b>
        <div className={styles.specialitiesField1}>
          <StyleOutlineTypetextClea
            label="Писать "
            styleOutlineTypetextCleaBorder="1px solid var(--color-steelblue-100)"
          />
          <StyleOutlineTypetextClea
            label="Считать"
            styleOutlineTypetextCleaBorder="1px solid var(--color-steelblue-100)"
          />
          <StyleOutlineTypetextClea
            label="Боксировать"
            styleOutlineTypetextCleaBorder="1px solid var(--color-steelblue-100)"
          />
        </div>
      </div>
    </div>
  );
};

export default FiltersBlock;
