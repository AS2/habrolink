import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./Homepage.module.css";
import HabrolinkerHeader from "../components/HabrolinkerHeader";
import { HasToken } from "../utils.jsx"

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
          <HabrolinkerHeader/>
          <div className={styles.background}>
              <div className={styles.welcome}>
                  <div className={styles.greetMsg}>
                      <p className={styles.greetLine}>
                          <span style={{fontWeight: 800}}>Хабролинкер </span>
                          <i style={{fontWeight: 500}}>[hɑbɹoʊˈɫɪŋkɝ]</i>
                          -
                      </p>
                      <p className={styles.greetLine}>
                          помощник в поисках
                          <i style={{fontWeight: 600}}> IT-единомышленников </i>
                      </p>
                      <p className={styles.greetLine}>
                          для
                          <i style={{fontWeight: 800}}> ваших </i>
                          проектов.
                      </p>
                      <p className={styles.greetLine}>&nbsp;</p>
                      <p className={styles.greetLine}>
                          Начните прямо
                          <span style={{fontWeight: 800}}> сейчас</span>
                          !
                      </p>
                      <p className={styles.greetLine}>&nbsp;</p>
                      <p className={styles.greetLine}>&nbsp;</p>
                  </div>
                  <div className={styles.greetButtons}>
                      <div
                          className={styles.searchButton}
                          onClick={onSearchButtonContainerClick}>
                          <b>Начать поиск</b>
                      </div>
                      { !HasToken() && <div
                          className={styles.signupButton}
                          onClick={onSignupButtonContainerClick}>
                          <b>Войти в систему</b>
                      </div> }
                  </div>
              </div>
          </div>
      </div>);
};

export default Homepage;
