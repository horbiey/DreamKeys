import { useState } from "react";

export default function AdForm() {
  const [photos, setPhotos] = useState([]);

  const handlePhotoUpload = (event) => {
    const files = Array.from(event.target.files);
    setPhotos(files.map(file => URL.createObjectURL(file)));
  };

  return (
    <div className="flex flex-col items-center min-h-screen bg-gray-900 text-white bg-cover bg-center" style={{ backgroundImage: "url('lyle-apartments-exterior.jpg')" }}>
      <header className="flex items-center justify-center gap-4 bg-gray-300 w-full py-4">
        <img src="665bd1c6-2cfb-40e2-a785-3e7c8fc9b1f3.jpg" alt="Логотип" className="w-12 h-12" />
        <h1 className="text-black text-xl font-bold">Створити оголошення</h1>
      </header>

      <div className="bg-gray-700 bg-opacity-80 p-6 rounded-lg w-96 mt-6">
        <form action="/submit-ad" method="POST" className="flex flex-col" encType="multipart/form-data">
          <label htmlFor="title" className="mt-2 text-sm">Описіть у подробицях*</label>
          <input type="text" id="title" name="title" placeholder="Наприклад, 2-кімнатна квартира в центрі міста" required className="mt-1 p-2 bg-white text-black border border-gray-300 rounded" />

          <label htmlFor="photos" className="mt-2 text-sm">Фото*</label>
          <input type="file" id="photos" name="photos" multiple accept="image/*" onChange={handlePhotoUpload} className="mt-1" />
          <div className="flex gap-2 mt-2 flex-wrap">
            {photos.map((src, index) => (
              <img key={index} src={src} alt="Uploaded" className="w-24 h-24 object-cover rounded border-2 border-gray-500 cursor-pointer" />
            ))}
          </div>

          <label htmlFor="description" className="mt-2 text-sm">Опис*</label>
          <textarea id="description" name="description" placeholder="Опис ключових характеристик квартири" required className="mt-1 p-2 bg-white text-black border border-gray-300 rounded resize-y h-24"></textarea>

          <label htmlFor="location" className="mt-2 text-sm">Місцезнаходження*</label>
          <input type="text" id="location" name="location" placeholder="Назва міста й індекс" required className="mt-1 p-2 bg-white text-black border border-gray-300 rounded" />

          <h2 className="text-lg font-semibold mt-4">Ваші контактні дані</h2>
          <label htmlFor="contact-name" className="mt-2 text-sm">Контактна особа*</label>
          <input type="text" id="contact-name" name="contact-name" required className="mt-1 p-2 bg-white text-black border border-gray-300 rounded" />

          <label htmlFor="phone" className="mt-2 text-sm">Номер телефону*</label>
          <input type="tel" id="phone" name="phone" required className="mt-1 p-2 bg-white text-black border border-gray-300 rounded" />

          <label htmlFor="email" className="mt-2 text-sm">Email - адреса*</label>
          <input type="email" id="email" name="email" required className="mt-1 p-2 bg-white text-black border border-gray-300 rounded" />

          <button type="submit" className="mt-4 p-2 bg-green-600 hover:bg-green-700 text-white font-semibold rounded">Опублікувати оголошення</button>
        </form>
      </div>
    </div>
  );
}
