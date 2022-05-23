using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerFire : MonoBehaviour
{
  // - 총알공장
  public GameObject bulletFactory;
  // - 총구위치
  public GameObject firePosition;

  // Start is called before the first frame update
  void Start()
  {

  }

  // Update is called once per frame
  void Update()
  {
    // 1. 만약 사용자가 마우스 왼쪽버튼을 누르면
    if (Input.GetButtonDown("Fire1"))
    {
      // 2. 총알공장에서 총알을 만들어서
      GameObject bullet = Instantiate(bulletFactory);
      // 3. 총구 위치에 가져다 놓고싶다.
      bullet.transform.position = firePosition.transform.position;
    }
  }
}
