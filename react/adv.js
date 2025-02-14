import React from "react";

const Header = () => (
  <div className="flex justify-between items-center mb-4">
    <div className="flex items-center">
      <img
        src="665bd1c6-2cfb-40e2-a785-3e7c8fc9b1f3.jpg"
        alt="DreamKeys Logo"
        className="h-10 mr-2"
      />
      <h2 className="text-xl font-bold">DreamKeys</h2>
    </div>
    <a href="#" className="bg-gray-300 px-3 py-1 rounded">⬅ назад</a>
  </div>
);

const InfoSection = () => (
  <div className="flex justify-between mt-4">
    <div className="flex-1 pr-4">
      <h3 className="text-lg font-semibold">Апартаменти</h3>
      <p>
        Сучасні апартаменти в центрі міста! Просторі, світлі, з ремонтом і меблями.
        Всі зручності для комфортного проживання.
      </p>
      <p>Київ, вул. Редутна.</p>
    </div>
    <div className="flex-1 bg-gray-200 p-4 rounded">
      <h3 className="text-lg font-semibold">22000$</h3>
      <h4 className="text-md font-semibold">Контактні дані</h4>
      <p>Номер телефону: +380 *** *** ****</p>
      <p>E-mail: example@gmail.com</p>
      <p>Ім'я: Іван Іванович Іванов</p>
    </div>
  </div>
);

const Footer = () => (
  <div className="flex justify-between mt-4">
    <div className="bg-gray-300 p-2 rounded">Площа об'єкту: 54 м²</div>
    <div className="bg-gray-300 p-2 rounded">Сучасний, середньомасштабний</div>
    <div className="bg-gray-300 p-2 rounded">Київ, вул. Редутна</div>
  </div>
);

const AnnouncementPage = () => {
  return (
    <div className="flex justify-center items-center min-h-screen bg-gray-900 text-white bg-cover" style={{ backgroundImage: "url(lyle-apartments-exterior.jpg)" }}>
      <div className="bg-gray-200 text-black p-6 rounded-lg w-[800px]">
        <Header />
        <img src="lyle-apartments-exterior.jpg" alt="Квартира" className="w-full rounded" />
        <InfoSection />
        <Footer />
      </div>
    </div>
  );
};

export default AnnouncementPage;

