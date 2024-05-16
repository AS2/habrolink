import { useCallback } from "react";
import Component from "../components/Component";
import { useNavigate } from "react-router-dom";
import styles from "./SignUp.module.css";

const SignUp = () => {
  const navigate = useNavigate();

  const onSaveContainerClick = useCallback(() => {
    navigate("/user-profile");
  }, [navigate]);

  const onTextClick = useCallback(() => {
    navigate("/");
  }, [navigate]);

  return (
    <div className={styles.signup}>
      <div className={styles.loginPage}>
        <div className={styles.userInfo}>
          <Component />
          <div className={styles.controllPart}>
            <div className={styles.save} onClick={onSaveContainerClick}>
              <div className={styles.div}>Сохранить изменения</div>
            </div>
          </div>
        </div>
      </div>
      <div className={styles.header}>
        <b className={styles.b} onClick={onTextClick}>
          <span>{`{`}</span>
          <span className={styles.span}>Хабро:</span>
          <span>{`Линкер}`}</span>
        </b>
        <img
          className={styles.interfaceEssentialmagnifier}
          alt=""
          src="/interface-essentialmagnifier.svg"
        />
      </div>
    </div>
  );
};

export default SignUp;
