import HabrolinkerTextField from "./HabrolinkerTextField";
import HabrolinkerPasswordFields from "./HabrolinkerPasswordFields";
import PwAgain from "./PwAgain";
import Gender from "./HabrolinkerEnumField";
import BDate from "./BDate";
import Salary from "./Salary";
import Skills from "./Skills";
import styles from "./Component.module.css";
import HabrolinkerEnumField from "./HabrolinkerEnumField";

const Component = () => {
  return (
    <div className={styles.div}>
      <div className={styles.topPart}>
        <div className={styles.div1}>
          <b className={styles.b}>Создание аккаунта</b>
        </div>
        <img className={styles.avatarIcon} alt="" src="/avatar.svg" />
      </div>
      <HabrolinkerTextField
        label="Логин"
        placeholder="tommy1884@mail.com"
        helperText="(11/100)"
      />
      <HabrolinkerPasswordFields />
      <PwAgain />
      <HabrolinkerTextField
        label="Полное имя"
        placeholder="Томас Шелби"
        helperText="(11/100)"
      />
      <HabrolinkerEnumField
        label="Пол"
        placeholder="Мужчина"
        standardChevronDown="/standard--chevrondown.svg"
      />
      <BDate />
      <HabrolinkerEnumField
        label="Страна"
        placeholder="Англия"
        standardChevronDown="/standard--select-dictionary.svg"
        propHeight="77px"
        propWidth="unset"
        propAlignSelf="stretch"
      />
      <HabrolinkerTextField label="Район" placeholder="Бирмингем" helperText="(9/100)" />
      <HabrolinkerTextField label="Город" placeholder="Смоллхит" helperText="(8/100)" />
      <Salary />
      <Skills
        label="Специальности"
        placeholder="Ведение бизнеса"
        helperText="Разные специальности необходимо разделять запятой"
      />
      <Skills
        label="Умения"
        placeholder="Скачки, Гадание, Софтскился"
        helperText="Разные умения необходимо разделять запятой"
      />
    </div>
  );
};

export default Component;
