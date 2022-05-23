using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DrawTriangle : MonoBehaviour
{
  // Start is called before the first frame update
  void Start()
  {
    string triangle = "";
    triangle += "*";
    triangle += '\n';
    triangle += "**";
    triangle += '\n';
    triangle += "***";
    triangle += '\n';
    triangle += "****";
    triangle += '\n';
    triangle += "*****";
    print(triangle);

    string triangle1 = "";
    for (int i = 0; i < 5; i++)
    {
      for (int j = 0; j < i + 1; j++)
      {
        triangle1 += "*";
      }
      triangle1 += '\n';
    }
    print(triangle1);
  }

  // Update is called once per frame
  void Update()
  {

  }
}
