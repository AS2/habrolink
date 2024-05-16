import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./Homepage.module.css";

const Homepage = () => {
  const navigate = useNavigate();

  const onSearchButtonContainerClick = useCallback(() => {
    navigate("/search-page");
  }, [navigate]);

  const onSignupButtonContainerClick = useCallback(() => {
    navigate("/signin");
  }, [navigate]);

  return (
    <div className={styles.homepage}>
      <div className={styles.background}>
        <img
          className={styles.imageDolboebovIcon}
          alt=""
          src="/image-dolboebov@2x.png"
        />
        <div className={styles.shadownOnImage} />
      </div>
      <div className={styles.welcome}>
        <div className={styles.hbokContainer}>
          <p className={styles.hbok}>
            <span className={styles.span}>{`Хабролинкер `}</span>
            <i className={styles.hbok1}>[hɑbɹoʊˈɫɪŋkɝ]</i>
            <span> -</span>
          </p>
          <p className={styles.hbok}>
            <span>{`помощник в поисках `}</span>
            <i className={styles.it1}>IT-единомышленников</i>
            <span className={styles.span1}>{`  для `}</span>
            <i className={styles.span}>ваших</i>
            <span> проектов.</span>
          </p>
          <p className={styles.hbok}>&nbsp;</p>
          <p className={styles.hbok}>
            <span>{`Начните прямо `}</span>
            <span className={styles.span}>сейчас</span>
            <span className={styles.span1}>!</span>
          </p>
        </div>
        <div
          className={styles.searchButton}
          onClick={onSearchButtonContainerClick}
        >
          <b className={styles.b}>Начать поиск</b>
        </div>
        <div
          className={styles.signupButton}
          onClick={onSignupButtonContainerClick}
        >
          <b className={styles.b}>Войти в систему</b>
        </div>
      </div>
      <div className={styles.header}>
        <b className={styles.b}>
          <span>{`{`}</span>
          <span className={styles.span4}>Хабро:</span>
          <span>{`Линкер}`}</span>
        </b>
      </div>
    </div>
  );
};

export default Homepage;
