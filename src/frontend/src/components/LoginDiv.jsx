import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import StateFilled from "./StateFilled";
import StyleFilledIconNoIconSt from "./StyleFilledIconNoIconSt";
import styles from "./LoginDiv.module.css";

const LoginDiv = () => {
  const navigate = useNavigate();

  const onButtonStyle1Click = useCallback(() => {
    navigate("/user-profile");
  }, [navigate]);

  const onText1Click = useCallback(() => {
    navigate("/signup");
  }, [navigate]);

  return (
    <div className={styles.loginDiv}>
      <b className={styles.b}>Войти в систему</b>
      <div className={styles.div}>
        <StateFilled
          labelText="Логин"
          prefix="$"
          inputText="tommy1884@mail.com"
          eye="/eye.svg"
          helperText="Helper Text"
          showHelperText={false}
          showPrefix={false}
          showIcon={false}
          stateFilledWidth="328px"
          stateFilledBorderRadius="20px"
          stateFilledFlex="unset"
          frameDivBackgroundColor="#fff"
          frameDivWidth="328px"
          helperTextWidth="328px"
          helperTextAlignSelf="unset"
        />
        <StateFilled
          labelText="Пароль"
          prefix="$"
          inputText="*************"
          eye="/eye-close.svg"
          helperText="Helper Text"
          showHelperText={false}
          showPrefix={false}
          showIcon
          stateFilledWidth="328px"
          stateFilledBorderRadius="20px"
          stateFilledFlex="unset"
          frameDivBackgroundColor="#fff"
          frameDivWidth="328px"
          helperTextWidth="328px"
          helperTextAlignSelf="unset"
        />
        <StyleFilledIconNoIconSt
          button="Войти"
          styleFilledIconNoIconStBackgroundColor="#2a6f97"
          buttonFontWeight="bold"
          onButtonStyle1Click={onButtonStyle1Click}
        />
      </div>
      <div className={styles.div1}>
        <i className={styles.b}>Нет записи?</i>
        <div className={styles.div2} onClick={onText1Click}>
          <span className={styles.span}>Создайте</span>
          <span> её.</span>
        </div>
      </div>
    </div>
  );
};

export default LoginDiv;
