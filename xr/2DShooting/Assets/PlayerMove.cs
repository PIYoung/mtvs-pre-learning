using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMove : MonoBehaviour
{
  public float speed = 5;

  // Start is called before the first frame update
  void Start()
  {

  }

  // Update is called once per frame
  void Update()
  {
    // 이동공식: P = P0 + vt
    // Vector
    // 크기와 방향을 갖는다.
    // 크기가 1인 벡터를 단위벡터 (normalized vector)라고 한다.
    // 더하기, 빼기, 곱하기(내적, 외적)의 연산이 가능하다.

    // DeltaTime
    // 화면을 한번 주사하는데 걸리는 시간
    // Update 함수 한번 도는데 걸린 시간
    // 다른 시스템간의 동기화를 위해 반드시 이동, 회전, 크기 변환에 곱해준다.
    // transform.position += Vector3.left * 5 * Time.deltaTime;

    // 1. 사용자의 입력에따라
    // 2. 방향을 만들고
    // 3. 그 방향으로 플레이어를 이동하고싶다.
    float h = Input.GetAxis("Horizontal");
    float v = Input.GetAxis("Vertical");
    // print(h); // -1 <= h <= 1
    Vector3 dir = Vector3.right * h + Vector3.up * v;
    // 문제발생!
    // 대각선 이동시 움직임의 크기가 더 크다.
    // 백터를 정규화 하고싶다.
    dir.Normalize();
    transform.position += dir * speed * Time.deltaTime;
  }
}
