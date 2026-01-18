export interface ServiceItem {
  id: string;
  title: string;
  description: string;
  image_url: string;
}

export interface ServiceCategory {
  id: string;
  title: string;
  items: ServiceItem[];
}

export const baseURL = import.meta.env.DEV ? 'http://localhost:8000' : (import.meta.env.VITE_API_BASE || 'https://your-backend-url.com')

export async function getServices(): Promise<ServiceCategory[]> {
  return servicesData;
}

export const servicesData: ServiceCategory[] = [
  {
    id: "core",
    title: "Core Cabinetry Services",
    items: [
      {
        id: "kitchen",
        title: "Custom Kitchen Cabinetry",
        description: "Tailored kitchen storage solutions designed for your culinary needs.",
        image_url: "https://loremflickr.com/600/400/kitchen,cabinet?random=1"
      },
      {
        id: "bathroom",
        title: "Bathroom Vanities",
        description: "Elegant and functional vanities to transform your bathroom.",
        image_url: "https://loremflickr.com/600/400/bathroom,vanity?random=2"
      },
      {
        id: "built-in",
        title: "Built-in Cabinets",
        description: "Seamless built-ins for living rooms, offices, and libraries.",
        image_url: "https://loremflickr.com/600/400/bookshelf,cabinet?random=3"
      },
      {
        id: "pantry",
        title: "Pantry Systems",
        description: "Organized pantry storage to maximize space and efficiency.",
        image_url: "https://loremflickr.com/600/400/pantry,shelves?random=4"
      },
      {
        id: "laundry",
        title: "Laundry Room Cabinetry",
        description: "Durable and accessible cabinetry for laundry areas.",
        image_url: "https://loremflickr.com/600/400/laundry,room?random=5"
      },
      {
        id: "mudroom",
        title: "Mudroom Storage",
        description: "Functional mudroom lockers and storage benches.",
        image_url: "https://loremflickr.com/600/400/mudroom,bench?random=6"
      },
      {
        id: "closet",
        title: "Closet Cabinetry",
        description: "High-end wood closet systems, superior to standard wire shelving.",
        image_url: "https://loremflickr.com/600/400/closet,clothes?random=7"
      },
      {
        id: "garage",
        title: "Garage Cabinets",
        description: "Heavy-duty wood or hybrid systems for garage organization.",
        image_url: "https://loremflickr.com/600/400/garage,tools?random=8"
      }
    ]
  },
  {
    id: "specialized",
    title: "Specialized Cabinet Work",
    items: [
      {
        id: "inset-overlay",
        title: "Inset, Overlay & Full-Overlay",
        description: "Various construction styles to match your aesthetic preference.",
        image_url: "https://loremflickr.com/600/400/cabinet,wood?random=9"
      },
      {
        id: "frameless",
        title: "Face-frame & Frameless",
        description: "Traditional face-frame or modern European frameless designs.",
        image_url: "https://loremflickr.com/600/400/modern,furniture?random=10"
      },
      {
        id: "drawers",
        title: "Custom Drawer Systems",
        description: "Premium dovetail joinery and soft-close mechanisms.",
        image_url: "https://loremflickr.com/600/400/drawer,wood?random=11"
      },
      {
        id: "panels",
        title: "Appliance Paneling",
        description: "Custom panels for dishwashers and refrigerators for a cohesive look.",
        image_url: "https://loremflickr.com/600/400/kitchen,fridge?random=12"
      },
      {
        id: "floating",
        title: "Floating Cabinets",
        description: "Modern wall-mounted cabinets that create an airy feel.",
        image_url: "https://loremflickr.com/600/400/floating,shelf?random=13"
      },
      {
        id: "island",
        title: "Island Cabinetry",
        description: "Custom center islands as the focal point of your kitchen.",
        image_url: "https://loremflickr.com/600/400/kitchen,island?random=14"
      },
      {
        id: "wine",
        title: "Wine Storage",
        description: "Temperature-stable and stylish wine racking and cabinetry.",
        image_url: "https://loremflickr.com/600/400/wine,rack?random=15"
      },
      {
        id: "display",
        title: "Display Cabinets",
        description: "Glass doors and integrated lighting to showcase your treasures.",
        image_url: "https://loremflickr.com/600/400/glass,cabinet?random=16"
      }
    ]
  }
];