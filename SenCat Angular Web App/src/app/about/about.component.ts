import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.css']
})
export class AboutComponent implements OnInit {
  members = [
    {
      name: 'Piyumal Demotte',
      imgURL: '../../assets/demotte.png'
    },
    {
      name: 'Lahiru Senevirathne',
      imgURL: '../../assets/lahiru.png'
    },
    {
      name: 'Binod Karunanayake',
      imgURL: '../../assets/binod.png'
    },
    {
      name: 'Udyogi Munasinghe',
      imgURL: '../../assets/udyogi.png'
    },
    // {
    //   name: 'Dr. Surangika Ranatunga',
    //   imgURL: '../../assets/sencat.png'
    // }
  ];

  constructor() { }

  ngOnInit(): void {
  }

}
