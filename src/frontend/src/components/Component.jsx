import City from "./City";
import Pw from "./Pw";
import PwAgain from "./PwAgain";
import Gender from "./Gender";
import BDate from "./BDate";
import Salary from "./Salary";
import Skills from "./Skills";
import styles from "./Component.module.css";

const Component = () => {
  return (
    <div className={styles.div}>
      <div className={styles.topPart}>
        <div className={styles.div1}>
          <b className={styles.b}>Создание аккаунта</b>
        </div>
        <img className={styles.avatarIcon} alt="" src="/avatar.svg" />
      </div>
      <City
        label="Логин"
        placeholder="tommy1884@mail.com"
        helperText="(11/100)"
      />
      <Pw />
      <PwAgain />
      <City
        label="Полное имя"
        placeholder="Томас Шелби"
        helperText="(11/100)"
      />
      <Gender
        label="Пол"
        placeholder="Мужчина"
        standardChevronDown="/standard--chevrondown.svg"
      />
      <BDate />
      <Gender
        label="Страна"
        placeholder="Англия"
        standardChevronDown="/standard--select-dictionary.svg"
        propHeight="77px"
        propWidth="unset"
        propAlignSelf="stretch"
      />
      <City label="Район" placeholder="Бирмингем" helperText="(9/100)" />
      <City label="Город" placeholder="Смоллхит" helperText="(8/100)" />
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
