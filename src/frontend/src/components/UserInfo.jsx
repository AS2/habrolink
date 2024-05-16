import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./UserInfo.module.css";

const UserInfo = () => {
  const navigate = useNavigate();

  const onTextClick = useCallback(() => {
    navigate("/user-profile-edit");
  }, [navigate]);

  return (
    <div className={styles.userInfo}>
      <b className={styles.b}>Аккаунт ХаброЛинкер</b>
      <div className={styles.topPart}>
        <div className={styles.div}>
          <b className={styles.b1}>Основная информация</b>
          <div className={styles.div1}>
            <div className={styles.habr}>Имя: Томас Шелби</div>
            <div className={styles.habr}>
              <span>{`Habr аккаунт: `}</span>
              <b>@tshelby</b>
            </div>
            <div className={styles.habr}>
              <span>{`Логин: `}</span>
              <b>tommy1884@mail.com</b>
            </div>
            <div className={styles.div4}>
              <div className={styles.div5}>Сменить логин</div>
              <div className={styles.div5}>Сменить пароль</div>
              <div className={styles.div5}>Сменить Хабр аккаунт</div>
            </div>
          </div>
        </div>
        <img className={styles.avatarIcon} alt="" src="/avatar.svg" />
      </div>
      <div className={styles.bottomPart}>
        <div className={styles.div8}>
          <b className={styles.b2}>Дополнительная информация</b>
          <div className={styles.div1}>
            <div className={styles.habr}>Пол: Мужчина</div>
            <div className={styles.habr}>
              <span>{`Дата рождения: `}</span>
              <b>20.01.1884</b>
            </div>
            <div className={styles.habr}>
              <span>{`Страна: `}</span>
              <b>Англия</b>
            </div>
            <div className={styles.habr}>
              <span>{`Город: `}</span>
              <b>Бирмингем</b>
            </div>
            <div className={styles.habr}>
              <span>{`Район: `}</span>
              <b>Смоллхит</b>
            </div>
            <div className={styles.habr}>
              <span>{`Доход: `}</span>
              <b>20’000’000£</b>
            </div>
            <div className={styles.habr}>
              <span>{`Рейтинг Хабра: `}</span>
              <b>5.0</b>
            </div>
            <div className={styles.habr}>
              <span>{`Карма Хабра: `}</span>
              <b>200</b>
            </div>
            <div className={styles.habr}>
              <span>{`Специальности: `}</span>
              <b>Ведение бизнеса</b>
            </div>
            <div className={styles.habr}>
              <span>{`Умения: `}</span>
              <b>Скачки, Гадание, Софтскилс</b>
            </div>
          </div>
        </div>
      </div>
      <div className={styles.controllPart}>
        <div className={styles.frame}>
          <div className={styles.div11} onClick={onTextClick}>
            Редактировать
          </div>
        </div>
      </div>
    </div>
  );
};

export default UserInfo;
