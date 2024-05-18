import { useCallback } from "react";
import HabrolinkerTextField from "./HabrolinkerTextField";
import Gender from "./HabrolinkerEnumField";
import BDate from "./BDate";
import Salary from "./Salary";
import Skills from "./Skills";
import { useNavigate } from "react-router-dom";
import styles from "./UserInfo1.module.css";

const UserInfo1 = () => {
  const navigate = useNavigate();

  const onSaveContainerClick = useCallback(() => {
    navigate("/user-profile");
  }, [navigate]);

  const onSaveContainer1Click = useCallback(() => {
    navigate("/user-profile");
  }, [navigate]);

  return (
    <div className={styles.userInfo}>
      <b className={styles.b}>Редактирование аккаунта</b>
      <div className={styles.div}>
        <HabrolinkerTextField
          label="Полное имя"
          placeholder="Томас Шелби"
          helperText="(11/100)"
        />
        <Gender
          label="Пол"
          placeholder="Мужчина"
          standardChevronDown="/standard--chevrondown.svg"
          propHeight="82px"
          propWidth="200px"
          propAlignSelf="unset"
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
      <div className={styles.controllPart}>
        <div className={styles.save} onClick={onSaveContainerClick}>
          <div className={styles.b}>Сохранить изменения</div>
        </div>
        <div className={styles.save1} onClick={onSaveContainer1Click}>
          <div className={styles.b}>Выйти без сохранения</div>
        </div>
      </div>
    </div>
  );
};

export default UserInfo1;
