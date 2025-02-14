import React from "react";

const apartments = [
  {
    id: 1,
    title: "1 ком квартира",
    location: "Запорожья, ул. Адерская",
    area: "23 м²",
    price: "25000$",
    image: "lyle-apartments-exterior.jpg",
  },
  {
    id: 2,
    title: "1 ком квартира",
    location: "Запорожья, ул. Адерская",
    area: "23 м²",
    price: "25000$",
    image: "lyle-apartments-exterior.jpg",
  },
  {
    id: 3,
    title: "1 ком квартира",
    location: "Запорожья, ул. Адерская",
    area: "23 м²",
    price: "25000$",
    image: "lyle-apartments-exterior.jpg",
  },
];

const Filters = () => (
  <aside className="w-1/5 bg-gray-100 p-5 shadow-md">
    <label className="font-bold">Купить квартиру</label>
    <select className="w-full p-2 mt-2 mb-4 border rounded">
      <option>Вся Украина</option>
    </select>

    <label className="font-bold">Количество комнат</label>
    <select className="w-full p-2 mt-2 mb-4 border rounded">
      <option>Одна</option>
    </select>

    <label className="font-bold">Цена</label>
    <input type="text" placeholder="От" className="w-full p-2 mt-2 border rounded" />
    <input type="text" placeholder="До" className="w-full p-2 mt-2 mb-4 border rounded" />

    <label className="font-bold">Площадь</label>
    <input type="text" placeholder="От" className="w-full p-2 mt-2 border rounded" />
    <input type="text" placeholder="До" className="w-full p-2 mt-2 border rounded" />
  </aside>
);

const ApartmentCard = ({ apartment }) => (
  <a href="#" key={apartment.id} className="border rounded shadow-md overflow-hidden flex">
    <img src={apartment.image} alt="Apartment" className="w-1/3" />
    <div className="p-4 w-2/3 bg-white flex flex-col justify-between">
      <h2 className="text-lg font-bold">{apartment.title}</h2>
      <p className="text-sm text-gray-600">{apartment.location}</p>
      <p className="text-sm text-gray-600">{apartment.area}</p>
      <p className="text-lg font-bold text-gray-900">{apartment.price}</p>
    </div>
  </a>
);

const Dreamkeys = () => (
  <div className="flex flex-col min-h-screen bg-cover bg-center" style={{ backgroundImage: "url('lyle-apartments-exterior.jpg')" }}>
    <header className="bg-gray-200 p-4 flex justify-between items-center">
      <div className="flex items-center">
        <img src="665bd1c6-2cfb-40e2-a785-3e7c8fc9b1f3.jpg" alt="Logo" className="w-10 h-10" />
        <h1 className="ml-3 text-2xl text-gray-800">Dreamkeys</h1>
      </div>
      <div className="flex space-x-4">
        <a href="#" className="text-gray-800 font-bold">Ваш профиль</a>
        <a href="#" className="text-red-600 font-bold">Подать объявление</a>
      </div>
    </header>

    <div className="flex flex-1 m-5">
      <Filters />
      
      <main className="flex-1 grid grid-cols-1 gap-6 p-6 md:grid-cols-2 lg:grid-cols-3">
        {apartments.map((apt) => (
          <ApartmentCard key={apt.id} apartment={apt} />
        ))}
      </main>
    </div>

    <footer className="bg-gray-800 text-white text-center p-4 mt-auto">
      <a href="#" className="mx-4">Facebook</a>
      <a href="#" className="mx-4">YouTube</a>
      <a href="#" className="mx-4">LinkedIn</a>
    </footer>
  </div>
);

export default Dreamkeys;

